import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dane/sprzedaz.csv", parse_dates=["data"])
df["przychod"] = df["ilosc"] * df["cena"]

miesiecznie = df.groupby(df["data"].dt.to_period("M"))["przychod"].sum()

miesiecznie.plot(kind="bar", color="#7c3aed", title="Przychód miesięcznie")
plt.ylabel("zł")
plt.tight_layout()
plt.savefig("wykres_przychod.png")
print(miesiecznie)
