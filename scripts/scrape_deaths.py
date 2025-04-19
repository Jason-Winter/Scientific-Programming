import requests
import pandas as pd
from io import StringIO

def download_bag_daily_deaths():
    print("🔍 Lade Link zu CSV von BAG...")

    # 1. Lade BAG-Kontext-JSON
    context_url = "https://www.covid19.admin.ch/api/data/context"
    context = requests.get(context_url).json()

    # 2. CSV-Link extrahieren
    deaths_csv_url = context["sources"]["individual"]["csv"]["daily"]["death"]
    print(f"📥 Lade CSV von: {deaths_csv_url}")

    # 3. Lade CSV und parse Inhalt
    csv_response = requests.get(deaths_csv_url)
    df = pd.read_csv(StringIO(csv_response.text))

    # 4. Filter & Umbenennung
    if "geoRegion" in df.columns and "datum" in df.columns and "sumTotal" in df.columns:
        df = df[df["geoRegion"] == "CH"]
        df = df[["datum", "sumTotal"]]
        df.columns = ["date", "total_deaths"]
    else:
        print("❌ Erwartete Spalten nicht gefunden.")
        return

    # 5. Datum als datetime
    df["date"] = pd.to_datetime(df["date"])

    # 6. Tägliche Todesfälle berechnen
    df["daily_deaths"] = df["total_deaths"].diff()
    df["daily_deaths"] = df["daily_deaths"].fillna(0).astype(int)  # Erste Zeile ist NaN → 0

    # 7. Speichern
    df.to_csv("data/bag_daily_deaths.csv", index=False)
    print("✅ BAG-Todesdaten mit täglicher Differenz gespeichert!")

if __name__ == "__main__":
    download_bag_daily_deaths()
