import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

wyniki=[]
for i in range(1,6):
    response=requests.get(f"https://www.olx.pl/motoryzacja/motocykle-skutery/q-motor/?page={i}", headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    ogloszenia = soup.find_all("div", attrs={"data-cy": "l-card"})
    for ogl in ogloszenia:
        try:
            nazwy=ogl.find("h4", class_="css-hzlye5").text
            ceny=ogl.find("p", class_="css-blr5zl")
            ceny=ceny.text.replace('do negocjacji', '')
            rocznik=ogl.find("span", class_="css-h59g4b").text
            wyniki.append({
                "Nazwa": nazwy,
                "Cena": ceny,
                "Rok": rocznik
            })
        except:
            continue


df = pd.DataFrame(wyniki)
print(df.head())

plt.figure(figsize=(10,15))
df["Cena"]=df["Cena"].str.replace(r'\D', '', regex=True)
df["Cena"]=df["Cena"].replace('','0')
df["Cena"]=df["Cena"].astype(int)

sns.scatterplot(x="Cena", y="Rok", data=df)
plt.title("Zalezność ceny od rocznika motocyklu z platformy OLX dla 5 stron ofert")
plt.show()

today = date.today()
df.to_csv(f"ceny_motocykli_{today}.csv", index=False)