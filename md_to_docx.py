"""Convert Pillage Campaign markdown files to DOCX via pandoc.

Outputs to ./docx/. Each .md file in the project root becomes a .docx with the same name.

Why pandoc and not LibreOffice's HTML conversion? Pandoc creates native Word tables
with proper auto-fit-to-window settings, so wide tables wrap properly within the page
margins. The earlier LibreOffice path didn't honor CSS table widths reliably.

Dependencies:
- pypandoc_binary (Python package; bundles the pandoc binary)
"""
import sys
from pathlib import Path

import pypandoc


def convert(md_path: Path, out_dir: Path):
    docx_path = out_dir / f"{md_path.stem}.docx"

    extra_args = [
        # Tighter page margins for more table room
        "-V", "geometry:margin=0.75in",
        # GitHub-flavored markdown (handles tables, fenced code, etc.)
        "--from=gfm+pipe_tables+footnotes",
        # Use a reference doc for default styling (optional; comment out if not present)
        # "--reference-doc=reference.docx",
    ]

    try:
        pypandoc.convert_file(
            str(md_path),
            "docx",
            outputfile=str(docx_path),
            extra_args=extra_args,
        )
    except Exception as exc:
        print(f"FAIL {md_path.name}: {exc}", file=sys.stderr)
        return False

    if docx_path.exists():
        print(f"OK   {docx_path.name} ({docx_path.stat().st_size:,} bytes)")
        return True
    print(f"FAIL {md_path.name}: no .docx produced", file=sys.stderr)
    return False


if __name__ == "__main__":
    base = Path(__file__).parent
    out_dir = base / "docx"
    out_dir.mkdir(exist_ok=True)

    files = sorted(base.glob("*.md"))
    if not files:
        print("No .md files found in project root.", file=sys.stderr)
        sys.exit(1)

    print(f"Converting {len(files)} markdown files to {out_dir}/ via pandoc\n")
    ok = sum(convert(f, out_dir) for f in files)
    print(f"\n{ok}/{len(files)} converted")
    sys.exit(0 if ok == len(files) else 1)
