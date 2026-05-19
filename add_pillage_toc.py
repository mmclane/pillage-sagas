"""Add PDF bookmarks (table of contents) to the Pillage rulebook.

Approach:
  1. Walk every PDF page and find the printed page number on it.
  2. Build a mapping from printed page number -> PDF page index.
  3. Use the printed Contents (entered below) to create bookmarks
     at the correct PDF pages.

Output: ./Sources/Pillage_A4_1.1.55_Digital_TOC.pdf
"""
import re
import sys
from pathlib import Path

import pypdf


SRC = Path(__file__).parent / "Sources" / "Pillage_A4_1.1.55_Digital.pdf"
OUT = Path(__file__).parent / "Sources" / "Pillage_A4_1.1.55_Digital_TOC.pdf"


# (title, printed_page, parent_title_or_None) — taken from the rulebook Contents.
TOC = [
    ("Foreword", 5, None),
    ("Generalities", 6, None),
    ("Introduction to the Early Middle Ages", 8, "Generalities"),
    ("Gaming Equipment", 14, "Generalities"),
    ("Setting Up A Game", 17, "Generalities"),
    ("Key Rules", 18, "Generalities"),

    ("Game Turn", 24, None),
    ("Initiative Phase", 25, "Game Turn"),
    ("Movement Phase", 26, "Game Turn"),
    ("Hit Rolls and Defence Rolls", 40, "Game Turn"),
    ("Shooting Phase", 42, "Game Turn"),
    ("Melee Phase", 48, "Game Turn"),
    ("Cavalry", 56, "Game Turn"),
    ("Fire Phase", 60, "Game Turn"),

    ("Advanced Rules", 64, None),
    ("Morale", 65, "Advanced Rules"),
    ("Pillage!", 66, "Advanced Rules"),
    ("Buildings", 70, "Advanced Rules"),
    ("Special Buildings", 73, "Advanced Rules"),
    ("Special Characters", 75, "Advanced Rules"),
    ("Chieftains", 75, "Special Characters"),
    ("Berserkers", 76, "Special Characters"),
    ("Huscarls", 77, "Special Characters"),
    ("Healers", 77, "Special Characters"),
    ("Supply Wagons", 78, "Special Characters"),
    ("Special Equipment", 79, "Advanced Rules"),
    ("Special Tactics", 82, "Advanced Rules"),
    ("Ships and Naval Battles", 84, "Advanced Rules"),
    ("Weather", 86, "Advanced Rules"),

    ("Factions", 88, None),
    ("Talents", 90, "Factions"),
    ("Vikings (Norse)", 94, "Factions"),
    ("Anglo-Saxons", 95, "Factions"),
    ("Normans", 96, "Factions"),
    ("Irish, Scots, and Picts", 97, "Factions"),
    ("Carolingian Franks", 98, "Factions"),
    ("Bretons", 99, "Factions"),
    ("Welsh", 100, "Factions"),
    ("Generic", 101, "Factions"),

    ("Playing The Game", 102, None),
    ("Multiple Players", 102, "Playing The Game"),
    ("Playing Pillage", 104, "Playing The Game"),
    ("Scenarios", 105, "Playing The Game"),
    ("Scenario 1: Pitched Battle", 106, "Playing The Game"),
    ("Scenario 2: Pillage!", 108, "Playing The Game"),
    ("Scenario 3: St. Brice's Day Massacre", 110, "Playing The Game"),
    ("Scenario 4: Landing", 112, "Playing The Game"),
    ("Scenario 5: Pilgrimage", 114, "Playing The Game"),

    ("Collecting", 116, None),
    ("Collecting an Army", 117, "Collecting"),
    ("Preparing Your Figures", 117, "Collecting"),
    ("Assembling Your Figures", 118, "Collecting"),
    ("Painting", 119, "Collecting"),
    ("Painting An Early Medieval Warrior", 120, "Collecting"),
    ("The Gaming Table", 123, "Collecting"),
    ("Making a Gaming Table", 123, "Collecting"),
    ("Making Simple Scenery", 124, "Collecting"),
    ("Reference Sheets, Tokens, And More", 130, "Collecting"),
]


def build_page_map(reader):
    """Map printed page number -> PDF page index (0-based).

    The Pillage PDF prints page numbers on the page. We extract each page's text
    and look for a small standalone integer near the page's edge text.
    """
    page_map = {}
    for i, page in enumerate(reader.pages):
        try:
            text = page.extract_text() or ""
        except Exception:
            continue
        # Look for numbers that appear on their own line, prefer small numbers
        # near the beginning or end of the extracted text (page numbers are
        # typically isolated). Take the smallest valid candidate.
        candidates = []
        for line in text.splitlines():
            line = line.strip()
            if line.isdigit():
                n = int(line)
                if 1 <= n <= 200:
                    candidates.append(n)
        if not candidates:
            continue
        # Heuristic: page numbers should roughly increase with PDF index.
        # Prefer the candidate closest to (PDF index - 2) (accounting for
        # 2 unnumbered front pages like cover + title).
        target = max(1, i - 1)
        best = min(candidates, key=lambda n: abs(n - target))
        # Only accept if reasonably close to target (sanity check)
        if abs(best - target) <= 5:
            page_map[best] = i
    return page_map


def main():
    if not SRC.exists():
        print(f"Source PDF not found: {SRC}", file=sys.stderr)
        return 1

    reader = pypdf.PdfReader(str(SRC))
    print(f"Pillage PDF has {len(reader.pages)} pages.\n")

    print("Building printed-page -> PDF-page map...")
    page_map = build_page_map(reader)
    print(f"Mapped {len(page_map)} printed pages.")

    # Show offset by checking some known printed pages
    if 5 in page_map and 64 in page_map:
        print(f"  printed p.5  -> PDF page {page_map[5] + 1}")
        print(f"  printed p.64 -> PDF page {page_map[64] + 1}")
        print(f"  printed p.94 -> PDF page {page_map.get(94, '?') + 1 if page_map.get(94) is not None else '?'}")
    print()

    writer = pypdf.PdfWriter(clone_from=reader)
    parent_handles = {}
    missing = []

    for title, printed_page, parent_name in TOC:
        pdf_idx = page_map.get(printed_page)
        if pdf_idx is None:
            # Try nearby pages as fallback
            for offset in (-1, 1, -2, 2):
                if (printed_page + offset) in page_map:
                    pdf_idx = page_map[printed_page + offset]
                    break
        if pdf_idx is None:
            print(f"  ?? could not map printed p.{printed_page}: {title}")
            missing.append(title)
            continue

        parent_handle = parent_handles.get(parent_name) if parent_name else None
        handle = writer.add_outline_item(title, pdf_idx, parent=parent_handle)
        parent_handles[title] = handle
        indent = "    " if parent_name else ""
        print(f"  {indent}p.{pdf_idx + 1:3d}  (printed {printed_page:3d})  {title}")

    OUT.parent.mkdir(exist_ok=True)
    with open(OUT, "wb") as f:
        writer.write(f)
    print(f"\nWrote: {OUT.relative_to(Path(__file__).parent)}")
    if missing:
        print(f"\n{len(missing)} entries could not be mapped:")
        for m in missing:
            print(f"  - {m}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
