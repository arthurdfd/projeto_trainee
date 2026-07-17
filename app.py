import streamlit as st
import pandas as pd
import joblib

# Configurações do painel
st.set_page_config(page_title="Predição de Preços - Regressão Linear", page_icon="🏠", layout="centered")

# Carregando o modelo de Regressão Linear
@st.cache_resource
def carregar_modelo_linear():
    return joblib.load('modelo_regressao_linear.joblib')

modelo_lr = carregar_modelo_linear()

# Título principal e descrição do contexto
st.title("🏠 Simulador de Preços de Imóveis")
st.markdown("""
Este aplicativo foi desenvolvido como parte do projeto final do processo de trainee da **CATI Jr.**
O painel utiliza o modelo de Regressão Linear para estimar o valor de mercado das casas com base em algumas características que a mesma apresenta.
""")

st.markdown("---")

# Divisão da tela em duas colunas para organizar
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🛠️ Estrutura e Espaço")
    gr_liv_area = st.number_input("Área Útil Acima do Solo (GrLivArea - sqft)", min_value=300, max_value=5000, value=1500, step=50)
    total_bsmt_sf = st.number_input("Área Total do Porão (TotalBsmtSF - sqft)", min_value=0, max_value=3000, value=1000, step=50)
    year_built = st.number_input("Ano de Construção (YearBuilt)", min_value=1870, max_value=2026, value=2000, step=1)

with col2:
    st.markdown("### ✨ Qualidade e Vagas")
    overall_qual = st.slider("Qualidade Geral do Acabamento (OverallQual - 1 a 10)", min_value=1, max_value=10, value=6)
    garage_cars = st.selectbox("Capacidade da Garagem (GarageCars - Carros)", [0, 1, 2, 3, 4], index=2)
    full_bath = st.selectbox("Quantidade de Banheiros Completos (FullBath)", [0, 1, 2, 3, 4], index=2)

st.markdown("---")

# Botão principal que dispara a execução do modelo
if st.button("📊 Estimar Preço de Venda", type="primary"):
    try:
        # Criando o dicionário estruturado com os dados de input
        dados_usuario = {
            'OverallQual': [overall_qual],
            'GrLivArea': [gr_liv_area],
            'GarageCars': [garage_cars],
            'TotalBsmtSF': [total_bsmt_sf],
            'FullBath': [full_bath],
            'YearBuilt': [year_built]
        }
        
        # Convertendo o dicionário para DF para que o modelo consiga fazer predict
        df_input = pd.DataFrame(dados_usuario)
        
        # Executando a Regressão Linear para obter o preço
        preco_predito = modelo_lr.predict(df_input)[0]
        
        # Exibindo o resultado formatado 
        # em dólares
        st.success("### Resultado da Simulação")
        st.markdown(f"O valor estimado de mercado para este imóvel é de: **$ {preco_predito:,.2f}**")
        
    except Exception as e:
        st.error(f"Erro ao processar a predição. Verifique novamente as variáveis. Detalhe: {e}")