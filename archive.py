from pathlib import Path
from datetime import datetime

ARCHIVE_DIR = Path("archive")


def archive_entry(raw_text: str, entry_date: str) -> Path:
    """
    Speichert den Original-Text in den archive-Ordner.
    """

    ARCHIVE_DIR.mkdir(exist_ok=True)

    file_path = ARCHIVE_DIR / f"{entry_date}.txt"

    if file_path.exists():
        timestamp = datetime.now().strftime("%H-%M-%S")
        file_path = ARCHIVE_DIR / f"{entry_date}_{timestamp}.txt"

    file_path.write_text(raw_text.strip() + "\n", encoding="utf-8")

    return file_path