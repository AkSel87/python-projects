from datetime import datetime

REQUIRED_FIELDS = {"Datum", "Zustand", "Erledigt", "Fokus", "Trigger", "Abweichung"}

DAY_NAMES_DE = {
    "Monday": "Montag",
    "Tuesday": "Dienstag",
    "Wednesday": "Mittwoch",
    "Thursday": "Donnerstag",
    "Friday": "Freitag",
    "Saturday": "Samstag",
    "Sunday": "Sonntag",
}


def parse_entry(raw_text: str) -> dict:
    """
    Wandelt den Journal-Textblock in ein Dictionary um.
    Beispiel:
        Datum: 2026-04-21
        Zustand: klar
        Erledigt: Ja
        Fokus: 7
        Trigger: Handy
        Abweichung: zu oft aufs Handy geschaut
    """
    entry = {}

    for line in raw_text.splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            entry[key.strip()] = value.strip()

    missing = REQUIRED_FIELDS - entry.keys()
    if missing:
        raise ValueError(f"Fehlende Felder: {', '.join(sorted(missing))}")

    try:
        date_obj = datetime.strptime(entry["Datum"], "%Y-%m-%d")
    except ValueError as error:
        raise ValueError("Datum muss im Format YYYY-MM-DD sein.") from error

    try:
        fokus = int(entry["Fokus"])
    except ValueError as error:
        raise ValueError("Fokus muss eine Zahl zwischen 1 und 10 sein.") from error

    if not 1 <= fokus <= 10:
        raise ValueError("Fokus muss zwischen 1 und 10 liegen.")

    erledigt_raw = entry["Erledigt"].strip().lower()
    if erledigt_raw not in {"ja", "nein"}:
        raise ValueError("Erledigt muss 'Ja' oder 'Nein' sein.")

    erledigt = "Ja" if erledigt_raw == "ja" else "Nein"
    score = fokus if erledigt == "Ja" else 0

    if score >= 8:
        status = "🔥 Stark"
    elif score >= 5:
        status = "⚡ Mittel"
    else:
        status = "❌ Schwach"

    day_name_en = date_obj.strftime("%A")
    iso_year, iso_week, _ = date_obj.isocalendar()

    return {
        **entry,
        "Erledigt": erledigt,
        "Fokus": fokus,
        "Score": score,
        "Status": status,
        "Wochentag": DAY_NAMES_DE.get(day_name_en, day_name_en),
        "ISO_Jahr": iso_year,
        "ISO_Woche": iso_week,
    }