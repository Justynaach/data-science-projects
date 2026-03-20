import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

results = []
for i in range(1, 6):
    url = f"https://www.olx.pl/motoryzacja/motocykle-skutery/q-motor/?page={i}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    listings = soup.find_all("div", attrs={"data-cy": "l-card"})
    for item in listings:
        try:
            name = item.find("h4", class_="css-hzlye5").text
            price_raw = item.find("p", class_="css-blr5zl").text

            price = price_raw.replace('do negocjacji', '').strip()
            year = item.find("span", class_="css-h59g4b").text
            
            results.append({
                "Model": name,
                "Price": price,
                "Year": year
            })
        except Exception as e:
            continue


df = pd.DataFrame(results)

df["Price"] = df["Price"].str.replace(r'\D', '', regex=True)
df["Price"] = df["Price"].replace('', '0').astype(int)

plt.figure(figsize=(10, 6))
sns.scatterplot(x="Price", y="Year", data=df)
plt.title("Motorcycle Price vs Year of Production (first 5 pages)")
plt.xlabel("Price [PLN]")
plt.ylabel("Production Year")
plt.show()

today = date.today()
df.to_csv(f"motorcycle_prices_{today}.csv", index=False)