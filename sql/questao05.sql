# Faturamento total por cliente
SELECT id_client, clientes.full_name, SUM(total) AS total_valor
FROM vendas 
JOIN clientes ON clientes.code = vendas.id_client
GROUP BY clientes.full_name;

#Contagem total de transações por cliente (Frequencia)
SELECT id_client, clientes.full_name, COUNT(id) AS total_vendas
FROM vendas
JOIN clientes ON clientes.code = vendas.id_client
GROUP BY id_client;

#Ticket médio de cada cliente
SELECT id_client, clientes.full_name, SUM(total) / COUNT(id) AS ticket_medio
FROM vendas
JOIN clientes ON clientes.code = vendas.id_client
GROUP BY id_client;

#Diversidade de categorias que cada cliente comprou
SELECT id_client, clientes.full_name, COUNT(DISTINCT p.actual_category) AS diferente_categorias
FROM vendas
JOIN clientes ON clientes.code = vendas.id_client
JOIN produtos p ON vendas.id_product = p.code
GROUP BY id_client;

#Top 10 clientes fiéis
SELECT id_client, COUNT(DISTINCT p.actual_category) AS diferente_categorias,
SUM(total) AS total_gasto, 
COUNT(id) AS total_vendas,
SUM(total) / COUNT(id) AS ticket_medio
FROM vendas v
JOIN produtos p ON v.id_product = p.code
GROUP BY id_client
HAVING COUNT(DISTINCT p.actual_category) >= 3
ORDER BY ticket_medio DESC
LIMIT 10;


#Produto que concentra a maior quantidade total de itens comprados no top 10 de clientes fiéis
SELECT p.actual_category AS categoria,
       SUM(v.quantity) AS total_itens
FROM vendas v
JOIN produtos p ON v.id_product = p.code
WHERE v.id_client IN (
    -- Subquery: os 10 clientes com maior ticket médio e 3+ categorias
    SELECT id_client
    FROM (
        SELECT v2.id_client
        FROM vendas v2
        JOIN produtos p2 ON v2.id_product = p2.code
        GROUP BY v2.id_client
        HAVING COUNT(DISTINCT p2.actual_category) >= 3
        ORDER BY SUM(v2.total)/COUNT(v2.id) DESC
        LIMIT 10
    ) AS top10
)
GROUP BY p.actual_category
ORDER BY total_itens DESC
LIMIT 1;
