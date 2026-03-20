import pandas as pd

df_produtos = pd.read_csv("/Users/sunset/Documents/lh-nautics-challenge/data/datasets-brutos/produtos_raw.csv", sep=',')

print("*-----------------DF SEM TRATAMENTO----------------------*")
print(df_produtos.info())
print(df_produtos.head())

print(" ")
print("*-----------------TRATAMENTO CAMPOS NUMÉRICOS----------------------*")

df_produtos['price'] = df_produtos['price'].str.replace('R$', '', regex=False)
df_produtos['price'] = df_produtos['price'].str.strip()
df_produtos['price'] = pd.to_numeric(df_produtos['price'])

print(df_produtos.info())
print(df_produtos.head())

print(" ")
print("*-----------------TRATAMENTO CATEGORIAS----------------------*")
df_produtos['actual_category'] = (df_produtos['actual_category']
    .str.lower()
    .str.strip()
    .str.replace(" ", "")
)

correcao_categorias = {
    'eletronicos': 'eletrônicos',
    'eletrônicos': 'eletrônicos',
    'eletrunicos': 'eletrônicos',
    'eletronicoz': 'eletrônicos',
    'eletroniscos': 'eletrônicos',

    'propulsao': 'propulsão',
    'propulção': 'propulsão',
    'prop': 'propulsão',
    'propulssão': 'propulsão',
    'propulsão': 'propulsão',
    'propução': 'propulsão',
    'propulçao': 'propulsão',
    'propulsam': 'propulsão',

    'ancoragem': 'ancoragem',
    'encoragem': 'ancoragem',
    'ancoraguem': 'ancoragem',
    'ancorajm': 'ancoragem',
    'ancorajem': 'ancoragem',
    'encoragi': 'ancoragem',
    'ancorajen': 'ancoragem',
    'ancoragen': 'ancoragem'
}

df_produtos['actual_category'] = df_produtos['actual_category'].replace(correcao_categorias)
print(df_produtos.head())
print("Categorias finais:", df_produtos['actual_category'].unique())

print(" ")
print("*------------------REMOVENDO DUPLICADOS---------------------*")
print("O dataframe possui " , df_produtos.duplicated().sum(), " registros duplicados")
df_produtos = df_produtos.drop_duplicates()

print(df_produtos.head())


df_produtos.to_csv("/Users/sunset/Documents/lh-nautics-challenge/data/datasets_tratados/produtos_tratados.csv", index=False)