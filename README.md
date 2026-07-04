# 🚤 LH Nautics Data Analysis

> Projeto desenvolvido como desafio técnico do processo seletivo do programa **Lighthouse**, da **Indicium AI**.

Este projeto teve como objetivo analisar um conjunto de dados de uma empresa fictícia do setor de varejo náutico, transformando dados brutos em informações estratégicas para apoiar a tomada de decisão.

A solução contempla todo o ciclo de análise de dados, desde a exploração inicial e tratamento dos dados até análises de negócio, previsão de demanda e desenvolvimento de um sistema de recomendação de produtos.

> **Resultado:** a solução desenvolvida foi aprovada no desafio técnico do programa Lighthouse, resultando no meu ingresso como **Data & AI Trainee** na **Indicium AI**.

---

# 📖 Contexto

A LH Nautics é uma empresa fictícia do setor de varejo náutico que enfrenta desafios relacionados à qualidade e integração dos seus dados.

Os dados disponibilizados apresentam inconsistências, diferentes formatos e ausência de padronização, dificultando análises confiáveis e a geração de insights para o negócio.

O objetivo deste projeto foi estruturar esses dados, responder perguntas estratégicas e desenvolver soluções analíticas utilizando SQL, Python e técnicas de Ciência de Dados.

---

# 🎯 Objetivos

- Realizar Análise Exploratória de Dados (EDA)
- Identificar problemas de qualidade dos dados
- Tratar e padronizar diferentes fontes de dados
- Analisar a rentabilidade dos produtos
- Identificar clientes de maior valor
- Avaliar padrões de vendas
- Desenvolver um modelo baseline para previsão de demanda
- Construir um sistema simples de recomendação de produtos

---

# 🛠 Tecnologias Utilizadas

- Python
- SQL
- Pandas
- Matplotlib
- Scikit-learn
- Requests
- JSON
- CSV
- API PTAX do Banco Central

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
│   ├── tratar_clientes.py
│   ├── tratar_produtos.py
│   ├── tratar_custos_importacao.py
│   ├── tratar_vendas.py
│   ├── obter_cotacao_dolar.py
│   ├── analisar_prejuizo_produtos.py
│   ├── prever_demanda_produto.py
│   └── recomendar_produtos.py
│
├── sql/
│   ├── explorar_dados_vendas.sql
│   ├── calcular_prejuizo_produtos.sql
│   ├── analisar_clientes.sql
│   └── analisar_vendas_semana.sql
│
└── README.md
```

---

# 🔄 Fluxo do Projeto

```text
               Dados Brutos
                      │
         ┌────────────┴────────────┐
         │                         │
     Exploração SQL        Tratamento Python
         │                         │
         └────────────┬────────────┘
                      │
              Dados Tratados
                      │
        ┌─────────────┼─────────────┐
        │             │             │
  Rentabilidade   Clientes      Vendas
        │             │             │
        └─────────────┼─────────────┘
                      │
          Previsão de Demanda
                      │
       Sistema de Recomendação
```

---

# 📊 Etapas Desenvolvidas

## 🔍 1. Análise Exploratória dos Dados (EDA)

A exploração inicial foi realizada utilizando **SQL**, permitindo compreender:

- volume de registros;
- período analisado;
- estatísticas descritivas;
- qualidade dos dados;
- inconsistências presentes no dataset.

Nesta etapa foram identificados problemas como:

- datas em formatos diferentes;
- registros incompletos;
- inconsistências de categorização;
- necessidade de padronização antes das análises.

---

## 🧹 2. Tratamento dos Dados

Foram desenvolvidos scripts em Python para tratamento e padronização das diferentes fontes de dados.

As principais transformações incluíram:

- padronização de categorias;
- conversão de tipos numéricos;
- tratamento de datas;
- remoção de registros duplicados;
- normalização de arquivos JSON;
- padronização de e-mails e localização dos clientes;
- preparação dos datasets para análise.

---

## 💰 3. Análise de Rentabilidade

Foi realizada a integração entre:

- vendas;
- custos de importação;
- cotação diária do dólar.

O objetivo foi identificar produtos comercializados abaixo do custo de importação.

### Principais insights

- Produtos vendidos com prejuízo significativo;
- Possíveis oportunidades de revisão da estratégia de precificação;
- Impacto da variação cambial na rentabilidade.

---

## 👥 4. Análise de Clientes

Foram analisados indicadores como:

- faturamento total;
- ticket médio;
- frequência de compras;
- diversidade de categorias adquiridas.

### Principais insights

- Receita concentrada em clientes de maior valor;
- Clientes com maior diversidade de compras apresentam maior potencial de retenção.

---

## 📅 5. Análise de Vendas

Foi analisado o comportamento das vendas ao longo da semana utilizando SQL e séries temporais.

### Principal insight

Os domingos apresentaram a menor média histórica de vendas, indicando oportunidade para ações comerciais específicas ou otimização operacional.

---

## 📈 6. Previsão de Demanda

Foi desenvolvido um modelo baseline utilizando **Média Móvel de 7 dias** para estimar a demanda diária de um produto.

A avaliação foi realizada utilizando a métrica **Mean Absolute Error (MAE)**, discutindo também as limitações da abordagem para produtos com baixa frequência de vendas.

---

## 🛒 7. Sistema de Recomendação

Foi implementado um sistema de recomendação baseado em **Similaridade do Cosseno**, utilizando uma matriz usuário × produto para identificar itens frequentemente adquiridos pelos mesmos clientes.

Exemplo:

> "Quem comprou este produto também comprou..."

---

# ⭐ Destaques Técnicos

Durante o desenvolvimento deste projeto foram utilizadas diferentes técnicas de análise e engenharia de dados, incluindo:

- Análise Exploratória de Dados (EDA) utilizando SQL;
- Tratamento e padronização de dados com Pandas;
- Normalização de estruturas JSON;
- Integração de múltiplas fontes de dados;
- Consumo da API PTAX do Banco Central;
- Consultas SQL utilizando CTEs, funções de janela e agregações;
- Análise de rentabilidade de produtos;
- Análise de comportamento de clientes;
- Modelo baseline de previsão de demanda;
- Sistema de recomendação baseado em Similaridade do Cosseno.

---

# 💡 Principais Insights

- Os dados apresentavam inconsistências que exigiram tratamento antes das análises.
- Foram identificados produtos comercializados abaixo do custo de importação.
- A receita apresentou concentração em um grupo reduzido de clientes.
- Domingos registraram o menor volume médio de vendas.
- O sistema de recomendação demonstrou potencial para estratégias de cross-selling.

---

# 🚀 Próximos Passos

Como evolução deste projeto, poderiam ser implementadas melhorias como:

- dashboards interativos em Power BI;
- automação do pipeline de dados;
- modelagem dimensional utilizando dbt;
- execução das transformações em ambiente Databricks.

---

# 👩‍💻 Autora

**Carla Lira Rodrigues**

**Analytics Engineering | SQL | dbt | Databricks | Data Modeling**

💼 LinkedIn: https://www.linkedin.com/in/carla-lira-rodrigues/

💻 GitHub: https://github.com/carlasunset