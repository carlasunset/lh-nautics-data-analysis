#Quantidade total de linhas 9901
SELECT COUNT(*) FROM vendas;

#Quantidade total de colunas 6 colunas
SELECT COUNT(*) AS total_colunas FROM information_schema.columns WHERE table_name = 'vendas';

#Intervalo de datas analisado (data mínima e máxima) - 01-01-2023 e 31-12-2024
SELECT MIN(sale_date) AS data_minima, MAX(sale_date) AS data_maxima FROM vendas;

#Valor mínimo 294,5
SELECT MIN(total) AS valor_minimo FROM vendas;

#Valor máximo - 2222973.00
SELECT MAX(total) AS valor_maximo FROM vendas;

#Valor médio - 263797.828267
SELECT AVG(total) AS valor_media FROM vendas;