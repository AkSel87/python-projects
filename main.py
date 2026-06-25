from parser import parse_entry
from storage import load_entries, save_entries, upsert_entry
from archive import archive_entry
from analysis import (average_score, most_common_trigger, best_day, worst_day, strongest_days_of_week, weakest_days_of_week,)
from plotting import plot_scores, plot_triggers

with open("heute.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()


entry = parse_entry(raw_text)

entries = load_entries()
entries = upsert_entry(entries, entry)
save_entries(entries)

print("Eintrag erfolgreich gespeichert.\n")

for saved_entry in entries:
    print("-" * 30)
    for key, value in saved_entry.items():
        print(f"{key}: {value}")
        
archive_path = archive_entry(raw_text, entry["Datum"])

print(f"\nArchiv gespeichert unter: {archive_path}")
avg_score = average_score(entries)
common_trigger = most_common_trigger(entries)
strongest = best_day(entries)
weakest = worst_day(entries)
strongest_week = strongest_days_of_week(entries, entry["ISO_Jahr"], entry["ISO_Woche"])
weakest_week = weakest_days_of_week(entries, entry["ISO_Jahr"], entry["ISO_Woche"])

print("\n--- ANALYSE ---")
print(f"Durchschnittlicher Score: {avg_score:.2f}")
print(f"Häufigster Trigger: {common_trigger}")

if strongest:
    print(f"Stärkster Tag: {strongest['Datum']} ({strongest['Score']})")

if weakest:
    print(f"Schwächster Tag: {weakest['Datum']} ({weakest['Score']})")
print(f"\n--- WOCHE {entry['ISO_Woche']} ---")

print("Stärkste Tage der Woche:")
for day in strongest_week:
    print(f"- {day['Datum']} | Score: {day['Score']} | Zustand: {day['Zustand']}")

print("Schwächste Tage der Woche:")
for day in weakest_week:
    print(f"- {day['Datum']} | Score: {day['Score']} | Zustand: {day['Zustand']}")

plot_scores(entries)
plot_triggers(entries)