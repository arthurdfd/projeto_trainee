# Projeto Final: House Prices - Predição de Preços e Clusterização de Imóveis

Projeto final do processo de trainee de dados da **CATI Jr.**

## Sobre o projeto

O objetivo é estimar o valor de venda de imóveis a partir de suas características físicas e de qualidade, usando o dataset [House Prices](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview) do Kaggle. Além da predição, o projeto também busca identificar perfis de imóveis por meio de clusterização, sem depender do preço como referência.

O projeto aplica os dois grandes tipos de aprendizado de máquina:

- **Aprendizado Supervisionado:** comparação entre Regressão Linear, Random Forest e Gradient Boosting (com otimização de hiperparâmetros) para prever `SalePrice`.
- **Aprendizado Não Supervisionado:** KMeans para segmentar os imóveis em grupos com características físicas semelhantes.

## Estrutura do repositório

```
.
├── data/
│   ├── train.csv
│   ├── test.csv
│   ├── data_description.txt
│   └── sample_submission.csv
├── app.py
├── modelo_regressao_linear.joblib
├── requirements.txt
├── projeto_final.ipynb
├── README.md
└── .gitignore
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

## Como rodar o aplicativo Streamlit

Para executar o simulador de preços interativo localmente, siga os passos abaixo no terminal:

1.  Ative o ambiente virtual (venv):
-   No Windows (Cmd): venv\Scripts\activate
-   No Windows (Git Bash): source venv/Scripts/activate
-   No Linux/macOS: source venv/bin/activate

2.  Certifique-se de ter as dependências instaladas:
-   pip install -r requirements.txt

3.  Inicie o servidor do Streamlit:
-   streamlit run app.py

## Tecnologias utilizadas

- Python
- Pandas / NumPy
- Matplotlib / Seaborn
- Scikit-learn
- Streamlit