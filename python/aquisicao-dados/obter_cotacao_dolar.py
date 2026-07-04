import requests
import pandas as pd

url = (
    "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
    "CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
    "?@dataInicial='01-01-2023'&@dataFinalCotacao='12-31-2024'"
    "&$top=10000&$format=json"
)

response = requests.get(url)
data = response.json()

df_cambio = pd.DataFrame(data['value'])
print(df_cambio.head())

df_cambio['data'] = pd.to_datetime(df_cambio['dataHoraCotacao']).dt.date

df_cambio = df_cambio.groupby('data')['cotacaoVenda'].mean().reset_index()

df_cambio.rename(columns={'data': 'sale_date', 'cotacaoVenda': 'exchange_rate'}, inplace=True)

print(df_cambio.head())

df_cambio.to_csv("cambio.csv", index=False)