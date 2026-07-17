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

# Carregando as colunas de treino do dataset original
@st.cache_resource
def carregar_colunas():
    return joblib.load("colunas_treino.joblib")

colunas_modelo = carregar_colunas()

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
        
        # Aqui, eu zero todas as colunas. Foi preciso fazer isso pois o modelo
        # de regressão original foi treinado com todas as colunas do dataset original.
        # Como eu só utilizo 6 para a predição aqui, é necessário lidar com o restante.
        dados_zerados = {col: [0] for col in colunas_modelo}
        df_input = pd.DataFrame(dados_zerados)
        
        # Substitui apenas as variáveis que são coletadas do usuário
        df_input['OverallQual'] = overall_qual
        df_input['GrLivArea'] = gr_liv_area
        df_input['TotalBsmtSF'] = total_bsmt_sf
        df_input['GarageCars'] = garage_cars
        df_input['FullBath'] = full_bath
        df_input['YearBuilt'] = year_built
        
        # Garante que a ordem das colunas esteja idêntica à do treinamento
        df_input = df_input[colunas_modelo]
        
        # Fazendo a predição
        preco_predito = modelo_lr.predict(df_input)[0]
        
        st.metric("Preço estimado", f"US$ {preco_predito:,.0f}")
    except Exception as e:
        st.error(f"Erro ao processar a predição. Detalhe técnico: {e}")