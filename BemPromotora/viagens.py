import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title='Dashboard de viagens')

# Dicionário com os datasets correspondentes a cada ano
datasets = {
    '2017': 'datasets/tabela_clean17.csv',
    '2018': 'datasets/tabela_clean18.csv',
    '2019': 'datasets/tabela_clean19.csv',
    '2020': 'datasets/tabela_clean20.csv',
    '2021': 'datasets/tabela_clean21.csv',
    '2022': 'datasets/tabela_clean22.csv'
}

# Sidebar
ano_selecionado = st.sidebar.selectbox('Selecione o ano', list(datasets.keys()))

# Carregar o dataset correspondente ao ano selecionado
dataset = pd.read_csv(datasets[ano_selecionado])


#Título
st.title("Viagens a Serviço")

# Organizando em linhas e colunas
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)



# Conteúdo da primeira coluna
with col1:
    fig_kind = px.pie(dataset, names="Meio_transporte", title="Meio de transporte")
    col1.plotly_chart(fig_kind, use_container_width=True)
    st.write()


with col2:
    fig_kind = px.pie(dataset, names="Realizada", title="A viagem foi realizada?")
    col2.plotly_chart(fig_kind, use_container_width=True)
    st.write()

  
with col3:
    fig_kind = px.pie(dataset, names="Missão", title="Houve missão?")
    col3.plotly_chart(fig_kind, use_container_width=True)
    st.write()


with col4:

    # Selecionar os 3 países mais frequentes, excluindo o Brasil
    paises_frequentes = dataset[dataset['Pais_destino_ida'] != 'Brasil']['Pais_destino_ida'].value_counts().head(3)
    fig_kind = px.bar(x=paises_frequentes.index, y=paises_frequentes.values, title="Países mais visitados")
    fig_kind.update_layout(xaxis_title="País", yaxis_title="Frequência")
    col4.plotly_chart(fig_kind, use_container_width=True)
    st.write()

with col5:
    cidades_frequentes = dataset['Cidade_destino_ida'].value_counts().head(3)
    fig_kind = px.bar(x=cidades_frequentes.index, y=cidades_frequentes.values, title="Cidades mais visitadas")
    fig_kind.update_layout(xaxis_title="Cidade", yaxis_title="Frequência")
    col5.plotly_chart(fig_kind, use_container_width=True)
    st.write()


with col6:
    uf_origem = dataset['UF_origem_ida'].value_counts().head(3)
    fig_kind = px.bar(x=uf_origem.index, y=uf_origem.values, title="UFs com mais partidas (origem)")
    fig_kind.update_layout(xaxis_title="UF", yaxis_title="Frequência")
    col6.plotly_chart(fig_kind, use_container_width=True)
    st.write()
    
    