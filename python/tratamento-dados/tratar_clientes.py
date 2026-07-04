import pandas as pd

df_clientes = pd.read_json("data/datasets-brutos/clientes_crm.json")

print("*-----------------DF SEM TRATAMENTO----------------------*")
print(df_clientes.info())
print(df_clientes[['location', 'email']])

print(" ")
print("*-----------------TRATAMENTO EMAIL----------------------*")
df_clientes['email'] = df_clientes['email'].str.replace('#', '@', regex=False)
print(df_clientes['email'])

print(" ")
print("*-----------------TRATAMENTO LOCATION----------------------*")
df_clientes['location'] = df_clientes['location'].str.strip()

df_clientes['location'] = (
    df_clientes['location']
    .str.replace('-', ',', regex=False)
    .str.replace('/', ',', regex=False)
)

df_clientes['location'] = df_clientes['location'].str.replace(' ,', ',', regex=False)
df_clientes['location'] = df_clientes['location'].str.replace(', ', ',', regex=False)
print(df_clientes['location'])

df_clientes.to_csv("data/datasets_tratados/clientes_tratados.csv", index=False)
