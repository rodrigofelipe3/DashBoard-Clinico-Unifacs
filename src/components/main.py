import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard" ,layout = "wide")
st.title("Dashboard Clínico")
st.write("Dados Estátisticos dos exames por cidade, bairro.")

#df
df = pd.read_csv("src\\assets\dados_exames_jan_a_abr_2024.csv", sep=";", encoding="cp1252",low_memory=False)

#APAGANDO AS LINHAS VAZIAS
#Removendo as cidades que não irão entrar no indice
df = df.dropna(how="any", axis=0)   
df = df.loc[df["CIDADE"]!="FEIRA DE SANTANA"]
df = df.loc[df["CIDADE"]!="FEIRA DE SANTAN"]
df = df.loc[df["CIDADE"]!="FEIRA"]
df = df.loc[df["CIDADE"]!="FSA"]
df = df.loc[df["CIDADE"]!="F", ["CIDADE", "QTDE", "EXAME", "BAIRRO", "CLINICA"]]
examDistrict = df.loc[df["EXAME"] == "M1"]
examforClinic = df.loc[df["EXAME"] == "UO"]

mostExamDistrict = examDistrict.groupby("BAIRRO")[["QTDE"]].sum().sort_values("QTDE", ascending = False).reset_index().head(10)
mostExameforCity = df.groupby("CIDADE")[["QTDE"]].sum().sort_values("QTDE", ascending = False).reset_index().head(10)
mostExame = df.groupby("EXAME")[["QTDE"]].sum().sort_values("QTDE", ascending = False).reset_index().head(10)
mostExameforClinic = examforClinic.groupby("CLINICA")[["QTDE"]].sum().reset_index().head(1)
totalForExam = df.groupby("EXAME")[["QTDE"]].sum().sort_values("QTDE", ascending = False).reset_index()
#DEFININDO O LAYOUT
col1, col2, col3 = st.columns(3)

#CRIANDO DASHBOARD
dash_City = px.bar(mostExameforCity, x ="CIDADE", y="QTDE", title="Gráfico das 10 cidades que mais realizaram exames")
col1.plotly_chart(dash_City, use_container_width=True)

#PLOT EXAMES MAIS REALIZADOS
dash_Exam = px.pie(mostExame, values="QTDE", names="EXAME", title="Gráfico dos 10 exames mais realizados")
col1.plotly_chart(dash_Exam, use_container_width=True)

#PLOT 10 BAIRROS QUE MAIS REALIZARAM EXAMES
dash_District = px.bar(mostExamDistrict, x="BAIRRO", y="QTDE", title="Gráfico dos 10 Bairros que mais realizaram exames" )
col2.plotly_chart(dash_District, use_container_width = True)

#PLOT UNIDADE QUE MAIS FEZ EXAME ULTRASSON OBSTETRICA
dash_Clinic = px.pie(mostExameforClinic, values="QTDE", names="CLINICA", title="UNIDADE QUE MAIS REALIZOU ULTRASSON OBISTETRICA")
col3.plotly_chart(dash_Clinic, use_container_width = True)

#total por Exame
dash_ForExam = px.bar(totalForExam, x="EXAME", y="QTDE", title="Gráfico do total por exame")
col2.plotly_chart(dash_ForExam, use_container_width = True)