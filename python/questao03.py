import pandas as pd

df_custos_importacao = pd.read_json("data/datasets-brutos/custos_importacao.json")
print("*-----------------DF SEM TRATAMENTO----------------------*")
print(df_custos_importacao.info())
print(df_custos_importacao.head())

print(" ")
print("*-----------------TRANSFORMANDO DE HISTORIC DATA PARA COLUNAS----------------------*")

df_explode = df_custos_importacao.explode('historic_data')

df_custos_normalizado = pd.json_normalize(df_explode['historic_data'])

df_final = pd.concat([df_explode[['product_id', 'product_name', 'category']].reset_index(drop=True),
                      df_custos_normalizado.reset_index(drop=True)], axis=1)
print(df_final.head())

print(" ")
print("*-----------------TRATAMENTO DAS DATAS----------------------*")
df_final['start_date'] = pd.to_datetime(df_final['start_date'], format='%d/%m/%Y')

print(df_final.head())
df_final.to_csv("data/datasets_tratados/custos_importacao_tratado.csv", index=False)


