import streamlit as st
from PIL import Image
import graphs as gph
from streamlit_folium import folium_static

def config_page():

    st.set_page_config(page_title = 'SARS-CoV-2',
                       page_icon = ":hospital:",
                       layout = "wide")

def home():
    img = Image.open("img/covid1.png")
    st.image(img, use_column_width='auto')

    with st.beta_expander("¿Quieres saber más?"):
        st.markdown('''Estudio realizado con datos científicos obtenidos de la página web del Instituto Carlos III desde el 01/01/2020 hasta el 09/03/2021.''')

        st.markdown('''En una primera etapa se ha analizado la sintomatología presente y posteriormente se ha evaluado el impacto en función del sexo y grupo
         de edad.''')

        st.markdown('''Se ha bajado hasta el nivel de CCAA obteniendo información del número de casos,
        número de hospitalizaciones, número de ingresos UCI y número de defunciones. Para lo cual se han 
        calculado indicadores como ratios, índice de mortalidad, índice de letalidad e incidencia acumulada a 14 y 7 días.''')

def sintomatología():
    st.markdown('''Encuesta realizada por la Sociedad Española de Médicos Generales y de Familia (SEMG) y 
        los colectivos de afectados LONG Covid ACTS entre el 13 de julio y el 14 de octubre del año 2020 a 2.120 infectados en la primera ola, 
        la mitad hombres y la otra parte mujeres.''')

    st.markdown('''De ellos, 1.843 son pacientes con sintomatología compatible con la COVID-19 persistente, con una media de 36 síntomas por persona; 
        y casi ocho de cada diez, el 79 por ciento, son mujeres con una media de edad de 43 años.''')

    st.markdown('''En la encuesta se recogen hasta 200 diferentes síntomas persistentes, aunque son 87 los más repetidos por los participantes. 
        Los más frecuentes son: cansancio/astenia (95,91 %); malestar general (95,47 %); dolores de cabeza (86,53 %); bajo estado de ánimo 
        (86,21 %); dolores musculares o mialgias (82,77 %); falta de aire o disnea (79,28 %); 
        dolores articulares (79 %); falta de concentración/déficit atención (78,24 %). 
        ''')

    st.markdown('''También el dolor de espalda (77,7 %); presión en el pecho (76,83 %); ansiedad (75,46 %); febrícula (75 %); tos (73,2 %); 
        fallos de memoria (72,63 %); dolor en el cuello/en las cervicales (71,32 %); diarrea (70,83 %); dolor torácico (70,12 %); 
        palpitaciones (69,85 %); mareos (69,36 %); y hormigueos en las extremidades o parestesias (67,28 %).
        ''')

    st.markdown('''La mitad de los encuestados tiene 7 áreas afectadas, lo más habitual con síntomas generales (95 %) y las alteraciones neurológicas 
        (86 %), seguidas de problemas psicológicos/emocionales (86 %), problemas del aparato locomotor (82 %) y respiratorios (79 %), 
        alteraciones digestivas (70%) y cardiovasculares (69%), entre otras.
        ''')

    st.markdown('''Aquí solamente se han recogido los 20 síntomas que más se han repetido en las personas encuestadas. 
        ''')

    with st.beta_expander('Ratio de pacientes con síntomas más frecuentes'):

        img = Image.open("img/síntomas_frecuentes.jpg")
        st.image(img, use_column_width='auto')

    with st.beta_expander('Ratio de pacientes con síntomas más incapacitantes'):

        img = Image.open("img/síntomas_más_incapacitantes.jpg")
        st.image(img, use_column_width='auto')

    with st.beta_expander('Comparativa pacientes con síntomas más frecuentes vs pacientes con síntomas más incapacitantes'):

        img = Image.open("img/comparativa.png")
        st.image(img, use_column_width='auto')

#        graph_sint_frec = gph.graph_sint_frec(gph.dffrec)
#        st.pyplot(graph_sint_frec)

def gráficos():
    with st.beta_expander('Ratio de casos, hospitalizaciones, ingresos UCI y defunciones por sexo'):

        graph_casos_sex = gph.graph_casos_sex(gph.df)
        st.plotly_chart(graph_casos_sex)

    with st.beta_expander('Ratio de casos, hospitalizaciones, ingresos UCI y defunciones por grupo de edad'):

        graph_casos_grup = gph.graph_casos_grup(gph.df1)
        st.plotly_chart(graph_casos_grup)

    with st.beta_expander('Número de casos por sexo y grupo de edad'):

        graph_casos_segr1 = gph.graph_casos_segr1(gph.df2)
        st.plotly_chart(graph_casos_segr1)

    with st.beta_expander('Número de hospitalizaciones por sexo y grupo de edad'):

        graph_casos_segr2 = gph.graph_casos_segr2(gph.df2)
        st.plotly_chart(graph_casos_segr2)

    with st.beta_expander('Número de ingresos UCI por sexo y grupo de edad'):

        graph_casos_segr3 = gph.graph_casos_segr3(gph.df2)
        st.plotly_chart(graph_casos_segr3)

    with st.beta_expander('Número de defunciones por sexo y grupo de edad'):

        graph_casos_segr4 = gph.graph_casos_segr4(gph.df2)
        st.plotly_chart(graph_casos_segr4)

    with st.beta_expander('Número de casos por CCAA'):

        graph_casos_ccaa = gph.graph_casos_ccaa(gph.df3)
        st.plotly_chart(graph_casos_ccaa)

    with st.beta_expander('Ratio de casos por CCAA'):

        graph_casos_ratio = gph.graph_casos_ratio(gph.df3)
        st.plotly_chart(graph_casos_ratio)

    with st.beta_expander('Número de hospitalizaciones por CCAA'):

        graph_hosp_ccaa = gph.graph_hosp_ccaa(gph.df4)
        st.plotly_chart(graph_hosp_ccaa)

    with st.beta_expander('Ratio de hospitalizaciones por CCAA'):

        graph_hosp_ratio = gph.graph_hosp_ratio(gph.df4)
        st.plotly_chart(graph_hosp_ratio)

    with st.beta_expander('Número de ingresos UCI por CCAA'):

        graph_uci_ccaa = gph.graph_uci_ccaa(gph.df4)
        st.plotly_chart(graph_uci_ccaa)

    with st.beta_expander('Ratio de ingresos UCI por CCAA'):

        graph_uci_ratio = gph.graph_uci_ratio(gph.df4)
        st.plotly_chart(graph_uci_ratio)

    with st.beta_expander('Número de defunciones por CCAA'):

        graph_def_ccaa = gph.graph_def_ccaa(gph.df4)
        st.plotly_chart(graph_def_ccaa)

    with st.beta_expander('Indice de mortalidad por CCAA (número defunciones/100.000 habitantes)'):

        graph_mort_ratio = gph.graph_mort_ratio(gph.df4)
        st.plotly_chart(graph_mort_ratio)

    with st.beta_expander('Indice de letalidad por CCAA (número defunciones/número de casos)'):

        graph_let_ratio = gph.graph_let_ratio(gph.df4)
        st.plotly_chart(graph_let_ratio)

    with st.beta_expander('Incidencia acumulada a 14 y 7 días'):

        graph_inc_acum = gph.graph_inc_acum(gph.df6)
        st.plotly_chart(graph_inc_acum)

    with st.beta_expander('Mapa con la incidencia acumulada a 14 días'):

        graph_map_acum = gph.graph_map_acum(gph.df6)
        folium_static(graph_map_acum)

    with st.beta_expander('Mapa con la incidencia acumulada a 7 días'):

        graph_map1_acum = gph.graph_map1_acum(gph.df6)
        folium_static(graph_map1_acum)

    with st.beta_expander('Número de defunciones los últimos 14 y 7 días'):

        graph_def_num = gph.graph_def_num(gph.df7)
        st.plotly_chart(graph_def_num)

