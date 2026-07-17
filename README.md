# Projeto Final: House Prices - Predição de Preços e Clusterização de Imóveis

Projeto final do processo de trainee de dados da **CATI Jr.**

## Sobre o projeto

O objetivo é estimar o valor de venda de imóveis a partir de suas características físicas e de qualidade, usando o dataset [House Prices](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview) do Kaggle. Além da predição, o projeto também busca identificar perfis de imóveis por meio de clusterização, sem depender do preço como referência.

O projeto aplica os dois grandes tipos de aprendizado de máquina:

- **Aprendizado Supervisionado:** comparação entre Regressão Linear, Random Forest e Gradient Boosting (com otimização de hiperparâmetros) para prever `SalePrice`.
- **Aprendizado Não Supervisionado:** KMeans para segmentar os imóveis em grupos com características físicas semelhantes.

## Estrutura do repositório

```
├── data/
│   ├── train.csv               # Conjunto de treino (features + SalePrice)
│   ├── test.csv                # Conjunto de teste (sem SalePrice, usado no Kaggle)
│   ├── data_description.txt    # Dicionário de dados com as 79 colunas explicativas
│   └── sample_submission.csv   # Formato de submissão exigido pelo Kaggle
├── projeto_final.ipynb         # Notebook principal com todo o desenvolvimento
├── .gitignore
└── README.md
```

## Roteiro do notebook

1. Importação de Bibliotecas
2. Carregamento e Inspeção dos Dados
3. Visualização Gráfica dos Dados
4. Análise de Qualidade dos Dados
5. Tratamento de Nulos
6. Tratamento de Outliers
7. Encoding de Variáveis Categóricas
8. Separação de Features e Target
9. Split de Treino e Teste
10. Modelo Supervisionado de Regressão Linear
11. Modelo de Ensemble - Random Forest
12. Modelo de Ensemble - Gradient Boosting
13. Otimização de Hiperparâmetros
14. Comparação Final dos Modelos
15. Clusterização (KMeans)
16. Conclusão

## Modelos utilizados

- **Regressão Linear** — melhor desempenho geral entre os modelos testados.
- **Random Forest** — modelo de ensemble.
- **Gradient Boosting** — modelo de ensemble, com versão padrão e versão otimizada via GridSearchCV.
- **KMeans** — segmentação dos imóveis em clusters por perfil físico.

## Tecnologias utilizadas

- Python
- Pandas / NumPy
- Matplotlib / Seaborn
- Scikit-learn
- Streamlit