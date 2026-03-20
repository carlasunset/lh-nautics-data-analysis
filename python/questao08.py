import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('/Users/sunset/Documents/lh-nautics-challenge/data/datasets_tratados/vendas_tratadas.csv')
df_produtos = pd.read_csv('/Users/sunset/Documents/lh-nautics-challenge/data/datasets_tratados/produtos_tratados.csv')


# Criar matriz usuário × produto
# Criar coluna binária (presença de compra)
df['comprou'] = 1

# Criar matriz pivot
matriz = df.pivot_table(
    index='id_client',
    columns='id_product',
    values='comprou',
    aggfunc='max',
    fill_value=0
)

# Similaridade produto × produto
# Transpor → produto vira linha
matriz_produto = matriz.T

# Calcular similaridade de cosseno
similaridade = cosine_similarity(matriz_produto)

# Transformar em DataFrame
df_similaridade = pd.DataFrame(
    similaridade,
    index=matriz_produto.index,
    columns=matriz_produto.index
)

# 4. Encontrar o GPS
gps_nome = 'GPS Garmin Vortex Maré Drift'

gps_row = df_produtos[df_produtos['name'] == gps_nome]

if gps_row.empty:
    raise ValueError("Produto não encontrado na tabela de produtos.")

gps_id = gps_row['code'].values[0]


# 5. Ranking de similares
ranking = df_similaridade[gps_id].sort_values(ascending=False)

# remover o próprio produto
ranking = ranking.drop(index=gps_id, errors='ignore')

top5 = ranking.head(5)

# 6. Trazer nomes dos produtos
top5_df = top5.reset_index()
top5_df.columns = ['id_product', 'similaridade']

top5_df = top5_df.merge(
    df_produtos[['code', 'name']],
    left_on='id_product',
    right_on='code',
    how='left'
)

top5_df = top5_df[['id_product', 'name', 'similaridade']]

print(top5_df)