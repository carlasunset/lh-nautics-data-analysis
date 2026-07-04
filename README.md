# 🚤 LH Nautics Data Analysis

Projeto desenvolvido como parte do **desafio técnico do processo seletivo do programa Lighthouse**, da **Indicium AI**.

O desafio consistiu em analisar um conjunto de dados de uma empresa fictícia do setor de varejo náutico, transformando dados brutos em informações estratégicas para apoiar a tomada de decisão.

A solução contempla desde a exploração e tratamento dos dados até análises de negócio, previsão de demanda e um sistema simples de recomendação de produtos.

> **Resultado:** este projeto foi um dos selecionados durante o processo seletivo, o que levou ao meu ingresso no programa **Lighthouse** como **Data & AI Trainee** na Indicium AI.

---

# 📖 Contexto

A LH Nautics é uma empresa do setor de varejo náutico que enfrenta desafios relacionados à qualidade e integração de seus dados.

Os dados disponíveis apresentam inconsistências, formatos distintos e ausência de padronização, dificultando análises confiáveis para apoiar decisões estratégicas.

O objetivo deste projeto foi estruturar esses dados e responder perguntas relevantes para o negócio através de técnicas de análise de dados.

---

# 🎯 Objetivos

- Realizar Análise Exploratória de Dados (EDA)
- Identificar problemas de qualidade dos dados
- Padronizar e tratar diferentes fontes de dados
- Analisar rentabilidade dos produtos
- Identificar clientes de maior valor
- Avaliar padrões de vendas
- Construir um modelo baseline de previsão de demanda
- Desenvolver um sistema simples de recomendação de produtos

---

# 🛠 Tecnologias Utilizadas

- Python
- SQL
- Pandas
- Matplotlib
- Scikit-learn
- JSON
- CSV
- API do Banco Central (cotação do dólar)

---

# 📁 Estrutura do Projeto

```text
.
├── data/
│   ├── datasets_brutos/
│   ├── datasets_tratados/
│   ├── cambio.csv
│   └── produtos_prejuizo.csv
│
├── notebooks/
│   └── lh_nautics_analysis.ipynb
│
├── python/
│   ├── clientes_crm.py
│   ├── produtos_prejuizo.py
│   ├── questao02.py
│   ├── questao03.py
│   ├── questao07.py
│   ├── questao08.py
│   ├── usd_bacen.py
│   └── vendas_2023_2024.py
│
├── sql/
│   └── questao01.sql
│
└── README.md
```

---

# 🔄 Fluxo do Projeto

```text
          Dados Brutos
                 │
        ┌────────┴────────┐
        │                 │
       SQL             Python
        │                 │
        └────────┬────────┘
                 │
        Tratamento dos Dados
                 │
          Dados Tratados
                 │
      ┌──────────┼──────────┐
      │          │          │
 Rentabilidade Clientes  Vendas
      │          │          │
      └──────────┼──────────┘
                 │
     Previsão de Demanda
                 │
    Sistema de Recomendação
```

---

# 📊 Etapas Desenvolvidas

## 🔍 1. Análise Exploratória (EDA)

A exploração inicial foi realizada utilizando **SQL**, permitindo compreender:

- volume de registros;
- qualidade dos dados;
- período das vendas;
- estatísticas descritivas;
- inconsistências presentes no dataset.

Nesta etapa foram identificados problemas como:

- datas em formatos diferentes;
- registros incompletos;
- possíveis outliers;
- necessidade de padronização antes das análises.

---

## 🧹 2. Tratamento dos Dados

Foram realizados tratamentos para tornar os dados consistentes, incluindo:

- padronização de categorias;
- conversão de tipos numéricos;
- tratamento de datas;
- remoção de duplicidades;
- normalização de arquivos JSON;
- preparação dos datasets para análise.

---

## 💰 3. Análise de Rentabilidade

Integração entre:

- vendas;
- custos de importação;
- cotação diária do dólar.

Objetivo:

Identificar produtos vendidos abaixo do custo e quantificar os prejuízos gerados.

### Principais insights

- Produtos vendidos com prejuízo significativo;
- Possível problema estrutural na estratégia de precificação;
- Necessidade de revisão de custos e margens.

---

## 👥 4. Análise de Clientes

Foram analisadas métricas como:

- faturamento;
- ticket médio;
- frequência de compras;
- diversidade de categorias.

### Principais insights

- Receita concentrada em clientes de maior valor;
- Clientes com maior diversidade de compras apresentam maior potencial de retenção.

---

## 📅 5. Análise de Vendas

Análise do comportamento das vendas ao longo da semana.

### Principal insight

Os domingos apresentaram a menor média histórica de vendas, indicando oportunidade para ações comerciais específicas ou otimização operacional.

---

## 📈 6. Previsão de Demanda

Foi desenvolvido um modelo baseline utilizando **Média Móvel de 7 dias** para estimar as vendas diárias de um produto.

### Avaliação

A performance foi avaliada utilizando **Mean Absolute Error (MAE)**.

Também foram discutidas as limitações do modelo para produtos com baixa frequência de vendas.

---

## 🛒 7. Sistema de Recomendação

Foi implementado um sistema simples de recomendação baseado em **Similaridade do Cosseno**.

O objetivo foi identificar produtos frequentemente adquiridos pelos mesmos clientes.

Exemplo:

> "Quem comprou este produto também comprou..."

---

# 💡 Principais Insights

- Os dados apresentavam inconsistências que exigiram tratamento antes das análises.
- Foram identificados produtos sendo comercializados abaixo do custo.
- A receita mostrou concentração em um grupo relativamente pequeno de clientes.
- Domingos apresentaram menor desempenho de vendas.
- O modelo de recomendação demonstrou potencial para estratégias de cross-selling.

---

# 🚀 Próximos Passos

Como evolução deste projeto, poderiam ser implementadas melhorias como:

- modelos de previsão utilizando Prophet ou XGBoost;
- dashboards interativos em Power BI;
- automação do pipeline de dados;
- modelagem dimensional com dbt;
- execução das transformações em ambiente Databricks.

---

# 👩‍💻 Autora

**Carla Lira Rodrigues**

Analytics Engineering | SQL | dbt | Databricks | Data Modeling

- 💼 LinkedIn: https://www.linkedin.com/in/carla-lira-rodrigues/
- 💻 GitHub: https://github.com/carlasunset
