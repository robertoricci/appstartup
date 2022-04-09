import pandas as pd
import streamlit as st
#import plotly.express as px

# função para carregar o dataset


@st.cache
def get_data():
    return pd.read_csv("venture_capital.csv")

st.set_page_config(page_title="Q&A Generator", page_icon="🎈")


# função para treinar o modelo
def train_model():
    data = get_data()
    data = data.drop(columns="Startup")

    # Separando os Dados de Treino e de Teste

    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    # Redimensionando os Dados - Padronização com o StandardScaler
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_trans = sc.fit_transform(X)

    # Treinamento da Máquina Preditiva
    #from sklearn.svm import SVC
    #Maquina_preditiva = SVC(kernel='linear', gamma=1e-5, C=10, random_state=7)
    #Maquina_preditiva.fit(X_trans, y)
    # return Maquina_preditiva

    # GradientBoostingClassifier:
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn import metrics
    Maquina_preditiva = GradientBoostingClassifier(n_estimators=3000)
    Maquina_preditiva.fit(X_trans, y)

    return Maquina_preditiva

    # Predictions:
    #y_pred = GradientBoost.predict(X_test)


# criando um dataframe
data = get_data()

# treinando o modelo
model = train_model()


st.sidebar.markdown("Redes Sociais :")
st.sidebar.markdown(
    "- [![Linkedin Badge](https://img.shields.io/badge/-%40robertoricci-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/roberto-carlos-ricci)](https://www.linkedin.com/in/roberto-carlos-ricci/)")

st.sidebar.markdown("- [![Portifolio Badge](https://img.shields.io/badge/-portif%C3%B3lio-yellow?style=flat-square&logo=powerbi&logoColor=white&link=https://robertoricci.github.io/pbisolutions.github.io/)](https://robertoricci.github.io/pbisolutions.github.io/)")

# título
st.title(
    "Indicação de Investimento em Startup com GradientBoosting    - By Roberto Carlos Ricci   ")

# subtítulo
st.markdown("Este é um Aplicativo utilizado para exibir a solução de Ciência de Dados para o problema de Investimentos em Startups em Venture Capital.")


st.sidebar.subheader("Insira os Dados dos Indicadores da Startup Avaliada ")

# mapeando dados do usuário para cada atributo
Indice_Faturamento = st.sidebar.number_input(
    "Indice de Faturamento", value=data.Indice_Faturamento.mean())
Indice_Setorial = st.sidebar.number_input(
    "Projecao Setorial", value=data.Indice_Setorial.mean())
Indice_Inovacao = st.sidebar.number_input(
    "Indice de Inovacao", value=data.Indice_Inovacao.mean())
Indice_Falencias = st.sidebar.number_input(
    "Indice de Falencias", value=data.Indice_Falencias.mean())
Indice_Expertise_Estrategica = st.sidebar.number_input(
    "Indicador de Expertise Estrategica", value=data.Indice_Expertise_Estrategica.mean())

# inserindo um botão na tela
btn_predict = st.sidebar.button("Avaliação da Startup Investida")


# verificando o dataset
st.subheader("Selecionando as Variáveis de Avaliação da Startup")

# atributos para serem exibidos por padrão
defaultcols = ['Indice_Faturamento', 'Indice_Setorial',
               'Indice_Inovacao', 'Indice_Falencias', 'Indice_Expertise_Estrategica']

# defindo atributos a partir do multiselect
cols = st.multiselect("Atributos", data.columns.tolist(), default=defaultcols)

# exibindo os top 8 registro do dataframe
st.dataframe(data[cols].head(7))


# verifica se o botão foi acionado
if btn_predict:
    result = model.predict([[Indice_Faturamento, Indice_Setorial,
                           Indice_Inovacao, Indice_Falencias, Indice_Expertise_Estrategica]])
    st.subheader("O Investimento na Startup é de :")
    result = result[0]
    st.write(result)
