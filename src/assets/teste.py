import streamlit as st
import pandas as pd
import plotly.express as px

#Configuração da Página
st.set_page_config(layout='wide')
st.title("Dashboard Exames Radiologicos")
st.write("Dados Estatísticos dos exames radiológicos")
#criar do Dataframe
df = pd.read_csv('dados_exames_jan_a_abr_2024.csv',sep=';',encoding="cp1252",low_memory=False)

#apagar as linhas com campos vazios
df = df.dropna(how='any',axis=0)
#Converter datas do tipo object para datetime
df['DATA'] = pd.to_datetime(df.DATA,errors = 'coerce')
#organizando 
df = df.sort_values("DATA")
df_novo = df[df['CIDADE']!='Feira de Santana']

#criando filtros para o dashboard
df["Meses"] = df['DATA'].apply(lambda x: str(x.year) + " - " + str(x.month))
mes = st.sidebar.selectbox("Mês",df["Meses"].unique())
df_filtered = df[df['Meses']==mes]

#Definindo layout do dashboard
col1, col2 = st.columns(2)
col3, col4,col5 = st.columns(3)

#atendimento_total = df_filtered.groupby("ATENDIMENTO")[['QTDE']].sum().reset_index()

dash_atendimento = px.pie(df_filtered,values="QTDE",names="ATENDIMENTO",title="Grafico por Tipo de Atendimento")
col1.plotly_chart(dash_atendimento,use_container_width=True)

exame_total = df_filtered.groupby("EXAME")[['QTDE']].sum().reset_index()
dash_exame = px.bar(exame_total,x="EXAME",y="QTDE",title="Grafico por Exames Realizados")
col2.plotly_chart(dash_exame,use_container_width=True)

bairro_total = df_filtered.groupby("BAIRRO")[['QTDE']].sum().reset_index()
dash_bairro = px.bar(bairro_total,x="BAIRRO",y="QTDE",title="Grafico por Bairro")
col3.plotly_chart(dash_bairro,use_container_width=True)

df_novo = df[df['CIDADE']!='Feira de Santana']

cidade_total = df_filtered.groupby("CIDADE")[['QTDE']].sum().reset_index()
dash_cidade = px.bar(cidade_total,x="CIDADE",y="QTDE",title="Grafico por Cidade")
col4.plotly_chart(dash_cidade,use_container_width=True)




