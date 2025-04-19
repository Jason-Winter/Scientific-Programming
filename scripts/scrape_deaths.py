import requests
import pandas as pd
from io import StringIO

def download_bag_daily_deaths():
    print("🔍 Lade Link zu CSV von BAG...")
    
    # 1. Hole Kontext mit Pfaden
    context_url = "https://www.covid19.admin.ch/api/data/context"
    context = requests.get(context_url).json()

    # 2. Korrekte CSV für Todesfälle pro Region
    deaths_csv_url = context["sources"]["individual"]["csv"]["daily"]["death"]

    print(f"📥 Lade CSV von: {deaths_csv_url}")

    # 3. Lade die CSV-Datei
    csv_response = requests.get(deaths_csv_url)
    df = pd.read_csv(StringIO(csv_response.text))

    # 4. Debug: Spalten anzeigen
    print("📌 Spalten gefunden:", list(df.columns))

    # 5. Filter für Schweiz
    if "geoRegion" in df.columns and "datum" in df.columns and "sumTotal" in df.columns:
        df = df[df["geoRegion"] == "CH"]
        df = df[["datum", "sumTotal"]]
        df.columns = ["date", "total_deaths"]
    else:
        print("❌ Erwartete Spalten nicht gefunden.")
        return

    # 6. Speichern
    df.to_csv("data/bag_daily_deaths.csv", index=False)
    print("✅ BAG-Todesdaten erfolgreich gespeichert!")

if __name__ == "__main__":
    download_bag_daily_deaths()
