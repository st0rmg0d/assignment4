import pandas as pd
import requests

r = requests.get("https://www.coingecko.com/en")

df = pd.read_html(r.text)[0]

df = df[["Coin", "Mkt Cap"]]

df["Coin"] = df["Coin"].apply(lambda x: x.split("  ")[0])


print(df)