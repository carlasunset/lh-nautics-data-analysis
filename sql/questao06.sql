WITH RECURSIVE calendario AS (
    SELECT (SELECT MIN(sale_date) FROM vendas_corretas) AS data

    UNION ALL

    SELECT DATE_ADD(data, INTERVAL 1 DAY)
    FROM calendario
    WHERE data < (SELECT MAX(sale_date) FROM vendas_corretas)
),

vendas_por_dia AS (
    SELECT 
        sale_date,
        SUM(total) AS total_dia
    FROM vendas_corretas
    GROUP BY sale_date
),

base AS (
    SELECT 
        c.data,
        COALESCE(v.total_dia, 0) AS total_dia,

        CASE DAYOFWEEK(c.data)
            WHEN 1 THEN 'Domingo'
            WHEN 2 THEN 'Segunda-feira'
            WHEN 3 THEN 'Terça-feira'
            WHEN 4 THEN 'Quarta-feira'
            WHEN 5 THEN 'Quinta-feira'
            WHEN 6 THEN 'Sexta-feira'
            WHEN 7 THEN 'Sábado'
        END AS dia_semana

    FROM calendario c
    LEFT JOIN vendas_por_dia v
        ON c.data = v.sale_date
)

SELECT 
    dia_semana,
    ROUND(AVG(total_dia), 2) AS media_vendas
FROM base
GROUP BY dia_semana
ORDER BY media_vendas ASC;
