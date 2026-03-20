import pandas as pd

df_vendas = pd.read_csv("../data/datasets-brutos/vendas_2023_2024.csv")
print("*-----------------DF SEM TRATAMENTO----------------------*")
print(df_vendas.info())
print(df_vendas.head())

print(" ")
print("*-----------------TRATAMENTO/PADRONIZAÇÃO DAS DATAS----------------------*")

def parse_data(data):
    data = str(data)

    # se começa com ano → já está no formato correto
    if data[:4].isdigit():
        return pd.to_datetime(data, format='%Y-%m-%d', errors='coerce')

    # senão → é dd-mm-yyyy
    return pd.to_datetime(data, format='%d-%m-%Y', errors='coerce')


df_vendas['sale_date'] = df_vendas['sale_date'].apply(parse_data)
df_vendas['sale_date'] = pd.to_datetime(df_vendas['sale_date'], errors='coerce')

df_vendas['sale_date'] = df_vendas['sale_date'].dt.strftime('%Y-%m-%d')

print(df_vendas.info())
print(df_vendas.head())
print("Data mais antiga", df_vendas['sale_date'].min())
print("Data mais recente", df_vendas['sale_date'].max())


df_vendas.to_csv("/Users/sunset/Documents/lh-nautics-challenge/data/datasets_tratados/vendas_tratadas.csv", index=False)