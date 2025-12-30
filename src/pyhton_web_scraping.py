import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from pathlib import Path


BASE = Path(__file__).resolve().parent
csv_putanja = BASE / "knjige_raw.csv"

sve_knjige = []


for stranica in range(1, 5):
    url = f"https://books.toscrape.com/catalogue/page-{stranica}.html"
    r = requests.get(url, headers={"User-Agent": "BookScraperBot/1.0"}, timeout=15)
    soup = BeautifulSoup(r.text, "html.parser")

    for k in soup.select(".product_pod"):
        naslov = k.h3.a["title"]
        cijena_txt = k.select_one(".price_color").get_text(strip=True)
        
        cijena = float(re.sub(r"[^\d.]", "", cijena_txt))
        dostupnost = k.select_one(".instock.availability").get_text(strip=True)

        sve_knjige.append({
            "naslov": naslov,
            "cijena": cijena,
            "dostupnost": dostupnost
        })

pd.DataFrame(sve_knjige).to_csv(csv_putanja, index=False)

print(f"Preuzeto {len(sve_knjige)} knjiga i spremljeno u '{csv_putanja}'")
