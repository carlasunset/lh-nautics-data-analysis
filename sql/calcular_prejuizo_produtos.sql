WITH vendas_com_prejuizo AS (
    SELECT
        v.id,
        v.id_product,
        v.sale_date,
        v.total AS valor_venda,

        ci.usd_price,
        c.exchange_rate,

        (ci.usd_price * c.exchange_rate) AS custo_brl,

        CASE 
            WHEN (ci.usd_price * c.exchange_rate) > v.total
            THEN (ci.usd_price * c.exchange_rate) - v.total
            ELSE 0
        END AS prejuizo,

        ROW_NUMBER() OVER (
            PARTITION BY v.id
            ORDER BY ci.start_date DESC
        ) AS rn
    FROM vendas v
    JOIN custos_importacao ci
        ON v.id_product = ci.product_id
        AND ci.start_date <= v.sale_date
    JOIN cambio c
        ON v.sale_date = c.sale_date
)
SELECT 
    id_product,
    SUM(valor_venda) AS receita_total,
    SUM(prejuizo) AS prejuizo_total,
    SUM(prejuizo) / SUM(valor_venda) AS percentual_perda
FROM vendas_com_prejuizo
WHERE rn = 1
GROUP BY id_product;