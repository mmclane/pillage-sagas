"""Convert Pillage Campaign markdown files to DOCX via Python-Markdown + LibreOffice headless.

Outputs to ./docx/. Each .md file in the project root becomes a .docx with the same name.
Upload the resulting .docx files into a single Google Doc and paste them into Tabs.
"""
import subprocess
import sys
from pathlib import Path

import markdown

SOFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"

CSS = """
<style>
@page { size: letter; margin: 1in; }
body { font-family: Calibri, 'Segoe UI', Arial, sans-serif; font-size: 11pt;
       line-height: 1.4; color: #000; max-width: 6.5in; }
h1 { font-size: 18pt; font-weight: bold; margin-top: 18pt; margin-bottom: 12pt;
     color: #1f3864; }
h2 { font-size: 14pt; font-weight: bold; margin-top: 14pt; margin-bottom: 8pt;
     border-bottom: 1px solid #999; padding-bottom: 2pt; color: #1f3864; }
h3 { font-size: 12pt; font-weight: bold; margin-top: 12pt; margin-bottom: 6pt;
     color: #2e5395; }
h4 { font-size: 11pt; font-weight: bold; margin-top: 10pt; margin-bottom: 4pt; }
p  { margin-top: 0; margin-bottom: 8pt; }
ul, ol { margin-top: 0; margin-bottom: 10pt; }
li { margin-bottom: 4pt; }
em { font-style: italic; }
strong { font-weight: bold; }
hr { border: 0; border-top: 1px solid #888; margin: 16pt 0; }
blockquote { border-left: 3px solid #888; margin: 10pt 0; padding: 0 12pt;
             color: #333; font-style: italic; }
table { border-collapse: collapse; margin: 10pt 0; font-size: 10pt; }
th, td { border: 1px solid #888; padding: 4pt 8pt; vertical-align: top; }
th { background-color: #d9e2f3; font-weight: bold; }
code { font-family: Consolas, 'Courier New', monospace; font-size: 10pt;
       background-color: #f0f0f0; padding: 1pt 3pt; }
pre { background-color: #f4f4f4; padding: 8pt; border: 1px solid #ddd;
      font-family: Consolas, 'Courier New', monospace; font-size: 9.5pt; }
a { color: #0563c1; text-decoration: underline; }
</style>
"""


def convert(md_path: Path, out_dir: Path):
    md_text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "footnotes", "attr_list", "sane_lists"],
    )
    html_doc = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{md_path.stem}</title>{CSS}</head>
<body>{html_body}</body></html>"""

    html_path = out_dir / f"{md_path.stem}.html"
    html_path.write_text(html_doc, encoding="utf-8")

    result = subprocess.run(
        [SOFFICE, "--headless", "--norestore",
         "--convert-to", "docx:MS Word 2007 XML",
         "--outdir", str(out_dir), str(html_path)],
        capture_output=True, text=True, timeout=120,
    )
    if result.returncode != 0:
        print(f"FAIL {md_path.name}:\n{result.stderr}", file=sys.stderr)
        return False

    html_path.unlink(missing_ok=True)
    docx_path = out_dir / f"{md_path.stem}.docx"
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

    print(f"Converting {len(files)} markdown files to {out_dir}/\n")
    ok = sum(convert(f, out_dir) for f in files)
    print(f"\n{ok}/{len(files)} converted")
    sys.exit(0 if ok == len(files) else 1)
