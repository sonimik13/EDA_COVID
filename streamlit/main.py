import streamlit as st
import functions as ft
import graphs as gph

ft.config_page()
st.title("Estudio de la evolución del SARS-CoV-2 en España")

menu = st.sidebar.selectbox("Seleccionar menú", ('página principal', 'sintomatología', 'situación diaria', 'gráficas'))

if menu == 'página principal':
    ft.home()

elif menu == 'sintomatología':
    ft.sintomatología()

elif menu == 'situación diaria':

    st.markdown('Gráfica que muestra la evolución diaria de casos COVID-19 en España y en cada CCAA')

    graph_sit_ccaa1 = gph.graph_sit_ccaa1(gph.df5)
    st.plotly_chart(graph_sit_ccaa1)

elif menu == 'gráficas':
    ft.gráficos()