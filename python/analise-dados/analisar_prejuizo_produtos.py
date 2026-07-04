import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/sunset/Documents/lh-nautics-challenge/data/produtos_prejuizo.csv", sep=";")
df.columns = df.columns.str.replace('"', '').str.strip()
colunas_numericas = ["receita_total", "prejuizo_total", "percentual_perda"]

for col in colunas_numericas:
    df[col] = df[col].astype(str).str.replace(",", ".")
    df[col] = pd.to_numeric(df[col], errors="coerce")

# filtrar
df_prejuizo = df[df["prejuizo_total"] > 0]

# ordenar
df_prejuizo = df_prejuizo.sort_values(by="prejuizo_total", ascending=False)

# gráfico
top10 = df_prejuizo.sort_values(by="prejuizo_total", ascending=False)

top10["acumulado"] = top10["prejuizo_total"].cumsum()
top10["percentual"] = top10["acumulado"] / top10["prejuizo_total"].sum()

plt.figure()

plt.bar(top10["id_product"].astype(str).head(20), top10["prejuizo_total"].head(20))
plt.xticks(rotation=45)

plt.twinx()
plt.plot(top10["id_product"].astype(str).head(20), top10["percentual"].head(20))

plt.title("Análise de Pareto - Prejuízo por produto")

plt.tight_layout()
plt.show()