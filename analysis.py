from collections import Counter


def average_score(entries: list) -> float:
    """
    Berechnet den durchschnittlichen Score aller Einträge.
    """
    if not entries:
        return 0.0

    scores = [entry["Score"] for entry in entries]
    return sum(scores) / len(scores)


def most_common_trigger(entries: list) -> str:
    """
    Findet den häufigsten Trigger.
    """
    triggers = [entry["Trigger"] for entry in entries if entry["Trigger"].strip()]
    if not triggers:
        return "Keiner"

    return Counter(triggers).most_common(1)[0][0]


def best_day(entries: list) -> dict | None:
    """
    Gibt den stärksten Tag zurück.
    """
    if not entries:
        return None

    return max(entries, key=lambda entry: entry["Score"])


def worst_day(entries: list) -> dict | None:
    """
    Gibt den schwächsten Tag zurück.
    """
    if not entries:
        return None

    return min(entries, key=lambda entry: entry["Score"])
def week_entries(entries: list, iso_year: int, iso_week: int) -> list:
    """
    Filtert alle Einträge für eine bestimmte ISO-Woche.
    """
    return [
        entry for entry in entries
        if entry["ISO_Jahr"] == iso_year and entry["ISO_Woche"] == iso_week
    ]


def strongest_days_of_week(entries: list, iso_year: int, iso_week: int) -> list:
    """
    Gibt alle stärksten Tage einer Woche zurück.
    """
    weekly = week_entries(entries, iso_year, iso_week)
    if not weekly:
        return []

    max_score = max(entry["Score"] for entry in weekly)
    return [entry for entry in weekly if entry["Score"] == max_score]


def weakest_days_of_week(entries: list, iso_year: int, iso_week: int) -> list:
    """
    Gibt alle schwächsten Tage einer Woche zurück.
    """
    weekly = week_entries(entries, iso_year, iso_week)
    if not weekly:
        return []

    min_score = min(entry["Score"] for entry in weekly)
    return [entry for entry in weekly if entry["Score"] == min_score]