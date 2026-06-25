from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path

PLOTS_DIR = Path("plots")
PLOTS_DIR.mkdir(exist_ok=True)

def plot_scores(entries: list):
    """
    Zeichnet den Score-Verlauf über die Zeit.
    """

    if not entries:
        print("Keine Daten zum Plotten vorhanden.")
        return

    # Daten sortieren nach Datum
    entries_sorted = sorted(entries, key=lambda e: e["Datum"])

    dates = [entry["Datum"] for entry in entries_sorted]
    scores = [entry["Score"] for entry in entries_sorted]

    # Plot erstellen
    plt.figure()
    plt.plot(dates, scores, marker="o")

    plt.title("Score Verlauf")
    plt.xlabel("Datum")
    plt.ylabel("Score")

    plt.xticks(rotation=45)
    plt.tight_layout()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    plt.savefig(PLOTS_DIR / f"score_{timestamp}.png")
    plt.show()
    plt.close()

def plot_triggers(entries: list):
    """
    Zeichnet ein Balkendiagramm für Trigger.
    """

    triggers = [entry["Trigger"] for entry in entries if entry["Trigger"].strip()]

    if not triggers:
        print("Keine Trigger-Daten vorhanden.")
        return

    counter = Counter(triggers)

    labels = list(counter.keys())
    values = list(counter.values())

    plt.figure()
    plt.bar(labels, values)

    plt.title("Trigger Häufigkeit")
    plt.xlabel("Trigger")
    plt.ylabel("Anzahl")

    plt.xticks(rotation=45)
    plt.tight_layout()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    plt.savefig(PLOTS_DIR / f"trigger_{timestamp}.png")
    plt.show()
    plt.close()