import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
headers = {"User-Agent": "Mozilla/5.0 (compatible; MyScraper/1.0"}
page = requests.get(url, headers=headers, timeout=10)
page.raise_for_status()

soup = BeautifulSoup(page.text, "lxml")
table = soup.find("table", class_="wikitable")

rows = table.find_all("tr")
header_cells = [th.get_text(strip=True) for th in rows[0].find_all("th")]

data = []
for r in rows[1:]:
    cols = [td.get_text(strip=True) for td in r.find_all(["td", "th"])]
    if cols and len(cols) == len(header_cells):
        data.append(cols)

df = pd.DataFrame(data, columns=header_cells)

df = df[["Rank", "Name", "Industry", "Revenue(USD millions)", "Revenue growth", "Headquarters"]]

df["Revenue(USD millions)"] = (
    df["Revenue(USD millions)"]
    .str.replace(r"\[.*?$]", "", regex=True)
    .str.replace(r"[$,]", "", regex=True)
    .astype("Int64")
)

df.to_csv("us_top_companies.csv", index=False)

print(df.head(100).to_string(index=False))

