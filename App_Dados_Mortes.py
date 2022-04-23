#executar no terminal: streamlit run App_Dados_Mortes.py

import streamlit as st
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static
import plotly
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd 
import numpy as np 
import requests

#==========================================================================================
st.title("Ednei Cunha Vicente - Cientista de Dados")
st.title("Web App com Dados do IBGE sobre Mortes Violentas que ocorreram no Brasil em 2019 - 2020 ")
st.write("**Mad By:[Ednei Cunha Vicente](https://www.linkedin.com/in/ednei-cunha-vicente-551b64187/")
st.write("**Mad By:[Ednei Cunha Vicente](https://github.com/ednei-code")

#=============================================================================================
#carrega os dados
df = pd.read_csv("dados/novo_df.csv")

#imprime o dataset
#st.dataframe(df)

#==========================================================================================
#mapas 
#Alagoas
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-9, -36, 1]])
).tolist()

Al = folium.Map([-9.513973,-36.624728],tiles="OpenStreetMap",zoom_start=5) #stamentoner
HeatMap(data).add_to(Al)
radius = 20
folium.CircleMarker(
    location=[-9.513973,-36.624728],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Alagoas Homicidio Doloso 2020 :  1218 casos"  
).add_to(Al)
#=========================================================================================
#Ceara
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-5, -39, 1]])
).tolist()

Ce = folium.Map([-5.093338, -39.615608],tiles="OpenStreetMap",zoom_start=5) #stamentoner
HeatMap(data).add_to(Ce)
radius = 20
folium.CircleMarker(
    location=[-5.093338	, -39.615608],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Ceara Homicidio Doloso 2020 :  3934 casos"  
).add_to(Ce)
#=============================================================================================
#distrito federal
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-15, -47, 1]])
).tolist()

distrito = folium.Map([-15.7807,-47.7973],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(distrito)
radius = 20
folium.CircleMarker(
    location=[-15.7807, -47.7973],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Distrito Federal Homicidio Doloso 2020 :  384 casos"  
).add_to(distrito)
#==========================================================================================================
#espirito santo
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-19, -40, 1]])
).tolist()

ES = folium.Map([-19.5751, -40.6708],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(ES)
radius = 20
folium.CircleMarker(
    location=[-19.5751, -40.6708],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Espirito Santo Homicidio Doloso 2020 :  1103 casos"  
).add_to(ES)
#==============================================================================================================
#Goias
#espirito santo
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-16, -49, 1]])
).tolist()

Go = folium.Map([-16.042109	,-49.623608],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(Go)
radius = 20
folium.CircleMarker(
    location=[-16.042109, -49.623608],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Goias Homicidio Doloso 2020 :  1468 casos"  
).add_to(Go)
#=====================================================================================================
#maranhao
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-5, -45, 1]])
).tolist()

Ma = folium.Map([-5.060433, -45.279153],tiles="OpenStreetMap",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(Ma)
radius = 20
folium.CircleMarker(
    location=[-5.060433, -45.279153],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Maranhao Homicidio Doloso 2020 :  1859 casos"  
).add_to(Ma)
#=========================================================================================================
#mato grosso
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-12, -55, 1]])
).tolist()

Mt = folium.Map([-12.948919, -55.911975],tiles="OpenStreetMap",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(Mt)
radius = 20
folium.CircleMarker(
    location=[-12.948919, -55.911975],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Mato Grosso Homicidio Doloso 2020 :  810 casos"  
).add_to(Mt)
##===========================================================================================================
#para
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-3, -53, 1]])
).tolist()

pr = folium.Map([-3.974815, -53.064197],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(pr)
radius = 20
folium.CircleMarker(
    location=[-3.974815	,-53.064197],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Pará Homicidio Doloso 2020 :  2176 casos"  
).add_to(pr)
#============================================================================================================
#paraiba
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-7, -36, 1]])
).tolist()

prb = folium.Map([-7.120898,-36.832085],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(prb)
radius = 20
folium.CircleMarker(
    location=[-7.120898, -36.832085],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Paraiba Homicidio Doloso 2020 :  1132 casos"  
).add_to(prb)
#===========================================================================================================
#parana
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-24, -51, 1]])
).tolist()

prn = folium.Map([-24.635840, -51.616400],tiles="OpenStreetMap",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(prn)
radius = 20
folium.CircleMarker(
    location=[-24.635840, -51.616400],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Parana Homicidio Doloso 2020 :  2008 casos"  
).add_to(prn)
#=========================================================================================================
#pernambuco
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-8, -37, 1]])
).tolist()

per = folium.Map([-8.326050, -37.998299],tiles="OpenStreetMap",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(per)
radius = 20
folium.CircleMarker(
    location=[-8.326050,-37.998299],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Pernambuco Homicidio Doloso 2020 :  3543 casos"  
).add_to(per)
#=============================================================================================================
#piaui
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-7, -42, 1]])
).tolist()

pi = folium.Map([-7.387435, -42.968494],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(pi)
radius = 20
folium.CircleMarker(
    location=[-7.387435,-42.968494],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Piaui Homicidio Doloso 2020 :  660 casos"  
).add_to(pi)
#===============================================================================================================
#Santa Catarina
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-27, -50, 1]])
).tolist()

sc = folium.Map([-27.247330, -50.474101],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(sc)
radius = 20
folium.CircleMarker(
    location=[-27.247330, -50.474101],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Santa Catarina Homicidio Doloso 2020 :  689 casos"  
).add_to(sc)
#=================================================================================================================
#sergipe
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-10, -37, 1]])
).tolist()

sg = folium.Map([-10.584717,-37.443872],tiles="OpenStreetMap",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(sg)
radius = 20
folium.CircleMarker(
    location=[-10.584717, -37.443872],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Sergipe Homicidio Doloso 2020 :  761 casos"  
).add_to(sg)
#=============================================================================================================
#bahia
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-12, -41, 1]])
).tolist()

ba = folium.Map([-12.475101,-41.720804],tiles="OpenStreetMap",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(ba)
radius = 20
folium.CircleMarker(
    location=[-12.475101, -41.720804],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Bahia Homicidio Doloso 2020 :  5368 casos"  
).add_to(ba)
#==============================================================================================================
#mato grosso do sul
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-20, -54, 1]])
).tolist()

mts = folium.Map([-20.327475, -54.8455644],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(mts)
radius = 20
folium.CircleMarker(
    location=[-20.327475, -54.845564],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Mato Grosso do Sul Homicidio Doloso 2020 :  467 casos"  
).add_to(mts)
#==============================================================================================================
#minas gerais
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-18, -44, 1]])
).tolist()

mg = folium.Map([-18.456155, -44.673385],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(mg)
radius = 20
folium.CircleMarker(
    location=[-18.456155, -44.673385],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Minas Gerais Homicidio Doloso 2020 :  2550 casos"  
).add_to(mg)
#===============================================================================================================
#Rio de janeiro
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-22, -42, 1]])
).tolist()

rj = folium.Map([-22.188569,-42.651667],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(rj)
radius = 20
folium.CircleMarker(
    location=[-22.188569, -42.651667],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Rio de Janeiro Homicidio Doloso 2020 : 3544 casos"  
).add_to(rj)
#===========================================================================================================
#rio grande do norte
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-5, -36, 1]])
).tolist()

rgn = folium.Map([-5.839525,-36.673283],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(rgn)
radius = 20
folium.CircleMarker(
    location=[-5.839525,-36.673283],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Rio Grande do Norte Homicidio Doloso 2020 :  1224 casos"  
).add_to(rgn)
#============================================================================================================
#rio grande do sul
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-29, -53, 1]])
).tolist()

rgs = folium.Map([-29.705809, -53.319974],tiles="OpenStreetMap",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(rgs)
radius = 20
folium.CircleMarker(
    location=[-29.705809, -53.319974],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Rio Grande do Sul Homicidio Doloso 2020 : 1780 casos"  
).add_to(rgs)
#====================================================================================================================
#sao paulo
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-22, -48, 1]])
).tolist()

sp = folium.Map([-22.263541, -48.733659],tiles="OpenStreetMap",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(sp)
radius = 20
folium.CircleMarker(
    location=[-22.263541, -48.733659],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Sao Paulo Homicidio Doloso 2020 : 3038 casos"  
).add_to(sp)
#======================================================================================================================
#tocantins
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-10, -48, 1]])
).tolist()

tc = folium.Map([-10.150000, -48.329160],tiles="OpenStreetMap",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(tc)
radius = 20
folium.CircleMarker(
    location=[-10.150000, -48.329160],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Tocantins Homicidio Doloso 2020 :  403 casos"  
).add_to(tc)
#================================================================================================================
#acre
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-9, -70, 1]])
).tolist()

ac = folium.Map([-9.212917, -70.473083],tiles="OpenStreetMap",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(ac)
radius = 20
folium.CircleMarker(
    location=[-9.212917, -70.473083],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Acre Homicidio Doloso 2020 :  280 casos"  
).add_to(ac)
#================================================================================================================
#amapa
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[1, -51, 1]])
).tolist()

am = folium.Map([1.443317, -51.956013],tiles="OpenStreetMap",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(am)
radius = 20
folium.CircleMarker(
    location=[1.443317, -51.956013],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Amapa Homicidio Doloso 2020 :  226 casos"  
).add_to(am)
#================================================================================================================
#amazonas
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-4, -64, 1]])
).tolist()

amz = folium.Map([-4.154223, -64.653187],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(amz)
radius = 20
folium.CircleMarker(
    location=[-4.154223, -64.653187],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Amazonas Homicidio Doloso 2020 :  954 casos"  
).add_to(amz)
#================================================================================================================
#rondonia
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[-10, -62, 1]])
).tolist()

rn = folium.Map([-10.913325, -62.841698],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(rn)
radius = 20
folium.CircleMarker(
    location=[-10.913325, -62.841698],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Rondonia Homicidio Doloso 2020 :  379 casos"  
).add_to(rn)
#======================================================================================================================
#roraima
data = (
    np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[2, -61, 1]])
).tolist()

rr = folium.Map([2.084090, -61.399162],tiles="stamentoner",zoom_start=5) #stamentoner #OpenStreetMap
HeatMap(data).add_to(rr)
radius = 20
folium.CircleMarker(
    location=[2.084090, -61.399162],
    radius=radius,
    color="blue",
    stroke=False,
    fill=True,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
    tooltip="Roraima Homicidio Doloso 2020 : 147 casos"  
).add_to(rr)
st.sidebar.subheader('Análise Através de Mapa')

select = st.sidebar.selectbox('Escolha o Tipo de Mapa',["Alagoas","Ceara","Distrito Federal","Espirito Santo",
	"Goias","Maranhao","Mato Grosso","Pará","Paraiba","Paraná","Pernambuco","Piaui","Santa Catarina","Sergipe",
	"Bahia","Mato Grosso do Sul","Minas Gerais","Rio de Janeiro","Rio Grande do Norte","Rio Grande do Sul","São Paulo",
	"Tocantins","Acre","Amapa","Amazonas","Rondonia","Roraima"], key = '1')

if not st.sidebar.checkbox("Ocultar Mapa",False):
	if select == "Alagoas":
		folium_static(Al)
	elif select == "Ceara":
		folium_static(Ce)
	elif select == "Distrito Federal":
		folium_static(distrito)
	elif select == "Espirito Santo":
		folium_static(ES)
	elif select == "Goias":
		folium_static(Go)
	elif select == "Maranhao":
		folium_static(Ma)
	elif select == "Mato Grosso":
		folium_static(Mt)
	elif select == "Pará":
		folium_static(pr)
	elif select == "Paraiba":
		folium_static(prb)
	elif select == "Paraná":
		folium_static(prn)
	elif select == "Pernambuco":
		folium_static(per)
	elif select == "Piaui":
		folium_static(pi)
	elif select == "Santa Catarina":
		folium_static(sc)
	elif select == "Sergipe":
		folium_static(sg)
	elif select == "Bahia":
		folium_static(ba)
	elif select == "Mato Grosso do Sul":
		folium_static(mts)
	elif select == "Minas Gerais":
		folium_static(mg)
	elif select == "Rio de Janeiro":
		folium_static(rj)
	elif select == "Rio Grande do Norte":
		folium_static(rgn)
	elif select == "Rio Grande do Sul":
		folium_static(rgs)
	elif select == "São Paulo":
		folium_static(sp)
	elif select == "Tocantins":
		folium_static(tc)
	elif select == "Acre":
		folium_static(ac)
	elif select == "Amapa":
		folium_static(am)
	elif select == "Amazonas":
		folium_static(amz)
	elif select == "Rondonia":
		folium_static(rn)
	elif select == "Roraima":
		folium_static(rr)


#==========================================================================================================
#criação dos grafico de barras com Plotly - Dash
st.sidebar.subheader("Análise com Grafico de Barras")

select = st.sidebar.selectbox("Escolha o gráfico de barras",
	['Crimes Violentos Letais Intencionais',"Policiais Civis e Militares Vitimas de Crimes",'Mortes Decorrentes de Intervenção Policial','Numero Absoluto'])

fig = go.Figure()

fig_1 = go.Bar(x = df['nome'],y=df["homicidio_Doloso_2020"],name="Homicido Doloso")
fig_2 = go.Bar(x= df['nome'],y=df["Latrocinio_2020"],name='Latrocinio')
fig_3 = go.Bar(x= df['nome'],y=df["Lesao_corporal_2020"],name="Lesao Corporal")

fig.add_traces([fig_1,fig_2,fig_3])

fig.update_layout(title_text='Crimes Violentos Letais Intencionais - CVLI',xaxis_tickangle=-45)

#=======================================================================================================================
fig_0 = go.Figure()

fig_1 = go.Bar(x = df['nome'],y=df["Policia_CVLI_2019"],name="2019")
fig_2 = go.Bar(x= df['nome'],y=df["Policia_CVLI_2020"],name='2020')

fig_0.add_traces([fig_1,fig_2])

fig_0.update_layout(title_text='Policiais Civis e Militares Vitimas de Crimes 2019 - 2020',xaxis_tickangle=-45)
#=======================================================================================================
fig_00 = go.Figure()

fig_1 = go.Bar(x = df['nome'],y=df["MDIP_2019"],name="2019")
fig_2 = go.Bar(x= df['nome'],y=df["MDIP_2020"],name='2020')

fig_00.add_traces([fig_1,fig_2])

fig_00.update_layout(title_text='Mortes Decorrentes de Intervenção Policial 2019 - 2020',xaxis_tickangle=-45)
#======================================================================================================================
fig_000 = go.Figure()

fig_1 = go.Bar(x = df['nome'],y=df["MVI_2019"],name="2019")
fig_2 = go.Bar(x= df['nome'],y=df["MVI_2020"],name='2020')

fig_000.add_traces([fig_1,fig_2])

fig_000.update_layout(title_text="Numero Absoluto 2019 - 2020",xaxis_tickangle=-45)

if select == 'Crimes Violentos Letais Intencionais':
	st.plotly_chart(fig)
elif select == "Policiais Civis e Militares Vitimas de Crimes":
	st.plotly_chart(fig_0)
elif select == "Mortes Decorrentes de Intervenção Policial":
	st.plotly_chart(fig_00)
elif select == "Numero Absoluto":
	st.plotly_chart(fig_000)  
#=======================================================================================================================
fig_0000 = go.Figure(data=[go.Scatter(
					x=df['nome'],y=df['Taxa_2020'],mode='markers')])
fig_0000.update_layout(title_text="Considera o Numero de Mortes por 100 Mil Habitantes", xaxis_tickangle=-45)
st.plotly_chart(fig_0000)
#=====================================================================================================================
st.subheader("Ceará e Bahia tem maiores taxas de mortes voilentas no país acima de 40 mortes por 100 mil habitantes.")
st.subheader("Entre os menos violentos, Santa Catarina se destaca junto com São Paulo - os unicos a registrar uma taxa abaixo de 12 mortes por 100 mil habitantes.")