import pandas as pd
from sklearn.metrics import mean_absolute_error

df_vendas = pd.read_csv('/Users/sunset/Documents/lh-nautics-challenge/data/datasets_tratados/vendas_tratadas.csv')
df_produtos = pd.read_csv('/Users/sunset/Documents/lh-nautics-challenge/data/datasets_tratados/produtos_tratados.csv')

# converter data foi necessário para podermos trabalhar com funções específicas de datas
df_vendas['sale_date'] = pd.to_datetime(df_vendas['sale_date'])

# aqui foi necessário fazer um merge de vendas com produtos,
# pois apenas nesse csv que encontramos o nome do produto
df = df_vendas.merge(
    df_produtos,
    left_on='id_product',
    right_on='code',
    how='left'
)

# manter só colunas necessárias pois aqui trabalharemos só com as informações contidas nelas
# isso reduz a complexidade do dataframe
df = df[['sale_date', 'name', 'qtd']]

# filtrar produto
produto_analisado = "Motor de Popa Yamaha Evo Dash 155HP"
df_produto = df[df['name'] == produto_analisado].copy()

# agrupar vendas por dia
df_daily = df_produto.groupby('sale_date')['qtd'].sum().reset_index()

# criar calendário completo
full_dates = pd.date_range(
    start=df_daily['sale_date'].min(),
    end=df_daily['sale_date'].max()
)

df_daily = df_daily.set_index('sale_date').reindex(full_dates, fill_value=0)
df_daily = df_daily.rename_axis('date').reset_index()

# separar treino e teste
train = df_daily[df_daily['date'] <= '2023-12-31'].copy()
test = df_daily[df_daily['date'] >= '2024-01-01'].copy()

# média móvel
train['ma7'] = train['qtd'].rolling(window=7).mean().shift(1)

# previsão
history = train[['date', 'qtd']].copy()

predictions = []

for i in range(len(test)):
    last_7_days = history['qtd'].iloc[-7:]
    pred = last_7_days.mean()

    predictions.append(pred)

    new_row = pd.DataFrame({
        'date': [test.iloc[i]['date']],
        'qtd': [pred]
    })

    history = pd.concat([history, new_row], ignore_index=True)

test['prediction'] = predictions

# MAE
mae = mean_absolute_error(test['qtd'], test['prediction'])
print("MAE:", mae)

# primeira semana
week1 = test[
    (test['date'] >= '2024-01-01') &
    (test['date'] <= '2024-01-07')
]

print(train.tail(10))
print(week1[['date', 'prediction']])
print(week1[['date', 'qtd']])

total_previsto = round(week1['prediction'].sum())
print(total_previsto)