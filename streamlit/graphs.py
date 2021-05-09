import pandas as pd
import folium as folium
import json
import plotly.express as px
import plotly.graph_objects as go
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots

#dffrec = pd.read_csv('data/sint_fre_ord.csv')

#def graph_sint_frec(dffrec):

    # Gráfica del ratio de pacientes con síntomas más frecuentes
#    graph_sint_frec = plt.figure(figsize=(4, 3))
#    plt.hlines(y=dffrec['síntomas más frecuentes'],
#               zorder=100,
#               xmin=40,
#               xmax=dffrec['% pacientes síntomas más frecuentes'],
#               color='skyblue')
#    plt.plot(dffrec['% pacientes síntomas más frecuentes'], dffrec['síntomas más frecuentes'], "o")
#    plt.subplots_adjust(left=0.35, bottom=0.1, right=0.95, top=0.8)
#    plt.title("Encuesta del SEMG realizada entre el 13/07/2020 y el 14/10/2020")
#    plt.xlabel('% pacientes síntomas más frecuentes', fontsize=5)
#    plt.ylabel("síntomas más frecuentes", fontsize=5)

#    return graph_sint_frec

df = pd.read_csv('data/casos_hosp_sex.csv')

def graph_casos_sex(df):

    '''
    Gráfica del ratio de casos, hospitalizaciones, ingresos UCI y defunciones por sexo
    '''

    x = df['sexo']

    trace1 = {
        'x': x,
        'y': df['porcentaje casos sexo'],
        'name': 'Casos',
        'type': 'bar'
    }

    trace2 = {
        'x': x,
        'y': df['porcentaje hospitalizaciones sexo'],
        'name': 'Hospitalizaciones',
        'type': 'bar'
    }

    trace3 = {
        'x': x,
        'y': df['porcentaje UCI sexo'],
        'name': 'UCI',
        'type': 'bar'
    }

    trace4 = {
        'x': x,
        'y': df['porcentaje defunciones sexo'],
        'name': 'Defunciones',
        'type': 'bar'
    }

    data = [trace1, trace2, trace3, trace4]
    layout = {'height': 500, 'width': 800,
#        'title': 'Ratio de casos, hospitalizaciones, ingresos UCI y defunciones por sexo',
        'xaxis': {'title': 'sexo'}
    }

    graph_casos_sex = go.Figure(data=data, layout=layout)

    return graph_casos_sex

df1 = pd.read_csv('data/casos_hosp_grup.csv')

def graph_casos_grup(df1):
    '''
    Ratio de casos, hospitalizaciones, ingresos UCI y defunciones por grupo de edad
    '''
    x = df1['grupo de edad']

    trace1 = {
        'x': x,
        'y': df1['porcentaje casos grupo'],
        'name': 'Casos',
        'type': 'bar'
    }

    trace2 = {
        'x': x,
        'y': df1['porcentaje hospitalizaciones grupo'],
        'name': 'Hospitalizaciones',
        'type': 'bar'
    }

    trace3 = {
        'x': x,
        'y': df1['porcentaje UCI grupo'],
        'name': 'UCI',
        'type': 'bar'
    }

    trace4 = {
        'x': x,
        'y': df1['porcentaje defunciones grupo'],
        'name': 'Defunciones',
        'type': 'bar'
    }

    data = [trace1, trace2, trace3, trace4]
    layout = {'height': 500, 'width': 800,
        'barmode': 'relative',
#        'title': 'Ratio de casos, hospitalizaciones, ingresos UCI y defunciones por grupo de edad',
        'xaxis': {'title': 'grupo de edad'}
    }

    graph_casos_grup = go.Figure(data=data, layout=layout)

    return graph_casos_grup

df2 = pd.read_csv('data/casos_hosp_segr.csv')

def graph_casos_segr1(df2):
    '''
    Número de casos por sexo y grupo de edad
    '''

    graph_casos_segr1 = go.Figure(data=go.Heatmap(
        z=df2['número de casos'],
        x=df2['grupo de edad'],
        y=df2['sexo'],
        hoverongaps=False))

    graph_casos_segr1.update_layout(
#        title='Número de casos por sexo y grupo de edad',
        xaxis_nticks=36)

    return graph_casos_segr1

def graph_casos_segr2(df2):

    '''
    Número de hospitalizaciones por sexo y grupo de edad
    '''
    graph_casos_segr2 = go.Figure(data=go.Heatmap(
        z=df2['número de hospitalizaciones'],
        x=df2['grupo de edad'],
        y=df2['sexo'],
        hoverongaps=False))

    graph_casos_segr2.update_layout(
#        title='Número de hospitalizaciones por sexo y grupo de edad',
        xaxis_nticks=36)

    return graph_casos_segr2

def graph_casos_segr3(df2):

    '''
    Número de ingresos UCI por sexo y grupo de edad
    '''
    graph_casos_segr3 = go.Figure(data=go.Heatmap(
        z=df2['número de ingresos UCI'],
        x=df2['grupo de edad'],
        y=df2['sexo'],
        hoverongaps=False))

    graph_casos_segr3.update_layout(
#        title='Número de ingresos UCI por sexo y grupo de edad',
        xaxis_nticks=36)

    return graph_casos_segr3

def graph_casos_segr4(df2):

    '''
    Número de defunciones por sexo y grupo de edad
    '''
    graph_casos_segr4 = go.Figure(data=go.Heatmap(
        z=df2['número de defunciones'],
        x=df2['grupo de edad'],
        y=df2['sexo'],
        hoverongaps=False))

    graph_casos_segr4.update_layout(
#        title='Número de defunciones por sexo y grupo de edad',
        xaxis_nticks=36)

    return graph_casos_segr4

df3 = pd.read_csv('data/df_merge_ccaa.csv')

def graph_casos_ccaa(df3):
    '''
    Número de casos por CCAA
    '''

    graph_casos_ccaa = px.treemap(df3, path=['comunidad'], values='número de casos', width=730, height=500)
    graph_casos_ccaa.data[0].hovertemplate = '%{label}<br>%{value}'

    graph_casos_ccaa.update_layout(
#        title='Número de casos CCAA',
        xaxis_nticks=36)

    return graph_casos_ccaa

def graph_casos_ratio(df3):

    # Ordeno de menor a mayor por la columna 'casos'
    df_merge_ccaa_mayor = df3.sort_values('casos')

    # Gráfica del ratio de casos por población y para cada CCAA
    x = df_merge_ccaa_mayor.comunidad

    trace = {
        'x': x,
        'y': df_merge_ccaa_mayor.casos,
        'name': 'casos',
        'type': 'bar'
    }

    data = trace
    layout = {'height': 600, 'width': 730,
        'barmode': 'relative',
#        'title': 'Ratio de casos CCAA',
        'xaxis': {'title': 'CCAA'}
    }

    graph_casos_ratio = go.Figure(data=data, layout=layout)
    graph_casos_ratio.update_xaxes(
            tickangle= 45
            )
    return graph_casos_ratio

df4 = pd.read_csv('data/df_merge_ccaa1.csv')

def graph_hosp_ccaa(df4):
    '''
    Número de hospitalizaciones por CCAA
    '''

    graph_hosp_ccaa = px.treemap(df4, path=['comunidad'], values='número de hospitalizaciones', width=730, height=500)
    graph_hosp_ccaa.data[0].hovertemplate = '%{label}<br>%{value}'

    graph_hosp_ccaa.update_layout(
#        title='Número de hospitalizaciones CCAA',
        xaxis_nticks=36)

    return graph_hosp_ccaa

def graph_hosp_ratio(df4):

    # Ordeno de menor a mayor por la columna 'casos'
    df_merge_ccaa_mayor = df4.sort_values('hospitalizaciones')

    # Gráfica del ratio de hospitalizaciones por población y para cada CCAA
    x = df_merge_ccaa_mayor.comunidad

    trace = {
        'x': x,
        'y': df_merge_ccaa_mayor.hospitalizaciones,
        'name': 'hospitalizaciones',
        'type': 'bar'
    }

    data = trace
    layout = {'height': 600, 'width': 730,
        'barmode': 'relative',
#        'title': 'Ratio de hospitalizaciones CCAA',
        'xaxis': {'title': 'CCAA'}
    }

    graph_hosp_ratio = go.Figure(data=data, layout=layout)
    graph_hosp_ratio.update_xaxes(
            tickangle= 45
            )
    return graph_hosp_ratio

def graph_uci_ccaa(df4):
    '''
    Número de ingresos UCI por CCAA
    '''

    graph_uci_ccaa = px.treemap(df4, path=['comunidad'], values='número de ingresos UCI', width=730, height=500)
    graph_uci_ccaa.data[0].hovertemplate = '%{label}<br>%{value}'

    graph_uci_ccaa.update_layout(
#        title='Número de ingresos UCI CCAA',
        xaxis_nticks=36)

    return graph_uci_ccaa

def graph_uci_ratio(df4):

    # Ordeno de menor a mayor por la columna 'casos'
    df_merge_ccaa_mayor = df4.sort_values('ingresos UCI')

    # Gráfica del ratio de ingresos UCI por población y para cada CCAA
    x = df_merge_ccaa_mayor.comunidad

    trace = {
        'x': x,
        'y': df_merge_ccaa_mayor['ingresos UCI'],
        'name': 'ingresos UCI',
        'type': 'bar'
    }

    data = trace
    layout = {'height': 600, 'width': 730,
        'barmode': 'relative',
#        'title': 'Ratio de ingresos UCI CCAA',
        'xaxis': {'title': 'CCAA'}
    }

    graph_uci_ratio = go.Figure(data=data, layout=layout)
    graph_uci_ratio.update_xaxes(
            tickangle= 45
            )
    return graph_uci_ratio

def graph_def_ccaa(df4):
    '''
    Número de defunciones por CCAA
    '''

    graph_def_ccaa = px.treemap(df4, path=['comunidad'], values='número de defunciones', width=730, height=500)
    graph_def_ccaa.data[0].hovertemplate = '%{label}<br>%{value}'

    graph_def_ccaa.update_layout(
#        title='Número de defunciones CCAA',
        xaxis_nticks=36)

    return graph_def_ccaa

def graph_mort_ratio(df4):
    '''
    Calculo el índice de mortalidad de cada CCAA (número de defunciones/100.000 habitantes)
    '''

    df4['índice de mortalidad'] = (
                df4['número de defunciones'] * 100000 / df4['población'])

    # Ordeno de menor a mayor por la columna 'índice de mortalidad'
    df_merge_ccaa1_mayor = df4.sort_values('índice de mortalidad')

    # Gráfica del índice de mortalidad por cada 10.000 habitantes y CCAA
    x = df_merge_ccaa1_mayor.comunidad

    trace = {
        'x': x,
        'y': df_merge_ccaa1_mayor['índice de mortalidad'],
        'name': 'índice de mortalidad',
        'type': 'bar'
    }

    data = trace
    layout = {'height': 600, 'width': 730,
        'barmode': 'relative',
#        'title': 'Indice de mortalidad en CCAA número defunciones/100.000 habitantes',
        'xaxis': {'title': 'CCAA'}
    }

    graph_mort_ratio = go.Figure(data=data, layout=layout)
    graph_mort_ratio.update_xaxes(
            tickangle= 45
            )
    return graph_mort_ratio

def graph_let_ratio(df4):
    '''
    Calculo el índice de letalidad para cada CCAA (número de defunciones/número de casos)
    '''

    df4['índice de letalidad'] = (df4['número de defunciones'] / df4['número de casos']) * 100

    # Ordeno de menor a mayor por la columna 'índice de letalidad'
    df_merge_ccaa1_mayor = df4.sort_values('índice de letalidad')

    #Gráfica del índice de letalidad para cada CCAA
    x = df_merge_ccaa1_mayor.comunidad

    trace = {
        'x': x,
        'y': df_merge_ccaa1_mayor['índice de letalidad'],
        'name': 'índice de letalidad',
        'type': 'bar'
    }

    data = trace
    layout = {'height': 600, 'width': 730,
        'barmode': 'relative',
#        'title': 'Indice de letalidad por CCAA (número defunciones/número de casos)',
        'xaxis': {'title': 'CCAA'}
    }

    graph_let_ratio = go.Figure(data=data, layout=layout)
    graph_let_ratio.update_xaxes(
            tickangle= 45
            )
    return graph_let_ratio

df5 = pd.read_csv('data/tec_ccaa.csv')

def graph_sit_ccaa1(df5):
    '''
    Genero los DataFrames de todas las CCAA
    '''

    dfMD = df5[df5.ccaa_iso == 'Comunidad de Madrid']
    dfRI = df5[df5.ccaa_iso == 'La Rioja']
    dfCL = df5[df5.ccaa_iso == 'Castilla y León']
    dfCM = df5[df5.ccaa_iso == 'Castilla-La Mancha']
    dfML = df5[df5.ccaa_iso == 'Melilla']
    dfAR = df5[df5.ccaa_iso == 'Aragón']
    dfNC = df5[df5.ccaa_iso == 'Comunidad Foral de Navarra']
    dfVC = df5[df5.ccaa_iso == 'Comunidad Valenciana']
    dfMC = df5[df5.ccaa_iso == 'Región de Murcia']
    dfPV = df5[df5.ccaa_iso == 'Euskadi']
    dfCT = df5[df5.ccaa_iso == 'Cataluña']
    dfEX = df5[df5.ccaa_iso == 'Extremadura']
    dfAN = df5[df5.ccaa_iso == 'Andalucía']
    dfCE = df5[df5.ccaa_iso == 'Ceuta']
    dfIB = df5[df5.ccaa_iso == 'Islas Baleares']
    dfAS = df5[df5.ccaa_iso == 'Principado de Asturias']
    dfCB = df5[df5.ccaa_iso == 'Cantabria']
    dfGA = df5[df5.ccaa_iso == 'Galicia']
    dfCN = df5[df5.ccaa_iso == 'Canarias']

    '''
     Sumo el 'num_casos', 'num_casos_prueba_pcr', 'num_casos_prueba_test_ac', 'num_casos_prueba_ag', 'num_casos_prueba_elisa'
     y 'num_casos_prueba_desconocida' para cada CCAA por fecha
     '''
    dfES = df5.groupby('fecha').agg({'num_casos': 'sum',
                                     'num_casos_prueba_pcr': 'sum',
                                     'num_casos_prueba_test_ac': 'sum',
                                     'num_casos_prueba_ag': 'sum',
                                     'num_casos_prueba_elisa': 'sum',
                                     'num_casos_prueba_desconocida': 'sum'}).reset_index()

    # Creating trace1. creamos primera linea
    trace1 = go.Scatter(x=dfES.fecha,
        y=dfES.num_casos,
        name="España",
        mode='lines',
        marker=dict(color='rgba(80, 26, 80, 0.8)'))

    # Creating trace2. creamos 2 línea
    trace2 = go.Scatter(
        x=dfMD.fecha,
        y=dfMD.num_casos,
        mode='lines',
        name='Comunidad de Madrid',
        marker=dict(color='rgba(16, 112, 2, 0.8)'))

    # Creating trace3. creamos 3 línea
    trace3 = go.Scatter(
        x=dfRI.fecha,
        y=dfRI.num_casos,
        mode='lines',
        name='La Rioja',
        marker=dict(color='rgba(153, 153, 0, 0.8)'))

    # Creating trace4. creamos 4 línea
    trace4 = go.Scatter(
        x=dfCL.fecha,
        y=dfCL.num_casos,
        mode='lines',
        name='Castilla y León',
        marker=dict(color='rgba(112, 157, 235, 0.8)'))

    # Creating trace5. creamos 5 línea
    trace5 = go.Scatter(
        x=dfCM.fecha,
        y=dfCM.num_casos,
        mode='lines',
        name='Castilla-La Mancha',
        marker=dict(color='rgba(255, 153, 51, 0.8)'))

    # Creating trace6. creamos 6 línea
    trace6 = go.Scatter(
        x=dfML.fecha,
        y=dfML.num_casos,
        mode='lines',
        name='Melilla',
        marker=dict(color='rgba(96, 96, 96, 0.8)'))

    # Creating trace7. creamos 7 línea
    trace7 = go.Scatter(
        x=dfAR.fecha,
        y=dfAR.num_casos,
        mode='lines',
        name='Aragón',
        marker=dict(color='rgba(153, 0, 153, 0.8)'))

    # Creating trace8. creamos 8 línea
    trace8 = go.Scatter(
        x=dfNC.fecha,
        y=dfNC.num_casos,
        mode='lines',
        name='Comunidad Foral de Navarra',
        marker=dict(color='rgba(51, 25, 0, 0.8)'))

    # Creating trace9. creamos 9 línea
    trace9 = go.Scatter(
        x=dfVC.fecha,
        y=dfVC.num_casos,
        mode='lines',
        name='Comunidad Valenciana',
        marker=dict(color='rgba(0, 204, 102, 0.8)'))

    # Creating trace10. creamos 10 línea
    trace10 = go.Scatter(
        x=dfMC.fecha,
        y=dfMC.num_casos,
        mode='lines',
        name='Región de Murcia',
        marker=dict(color='rgba(255, 51, 51, 0.8)'))

    # Creating trace11. creamos 11 línea
    trace11 = go.Scatter(
        x=dfPV.fecha,
        y=dfPV.num_casos,
        mode='lines',
        name='Euskadi',
        marker=dict(color='rgba(0, 0, 255, 0.8)'))

    # Creating trace12. creamos 12 línea
    trace12 = go.Scatter(
        x=dfCT.fecha,
        y=dfCT.num_casos,
        mode='lines',
        name='Cataluña',
        marker=dict(color='rgba(32, 32, 32, 0.8)'))

    # Creating trace13. creamos 13 línea
    trace13 = go.Scatter(
        x=dfEX.fecha,
        y=dfEX.num_casos,
        mode='lines',
        name='Extremadura',
        marker=dict(color='rgba(102, 0, 51, 0.8)'))

    # Creating trace14. creamos 14 línea
    trace14 = go.Scatter(
        x=dfAN.fecha,
        y=dfAN.num_casos,
        mode='lines',
        name='Andalucía',
        marker=dict(color='rgba(0, 51, 51, 0.8)'))

    # Creating trace15. creamos 15 línea
    trace15 = go.Scatter(
        x=dfCE.fecha,
        y=dfCE.num_casos,
        mode='lines',
        name='Ceuta',
        marker=dict(color='rgba(240, 128, 0, 0.8)'))

    # Creating trace16. creamos 16 línea
    trace16 = go.Scatter(
        x=dfIB.fecha,
        y=dfIB.num_casos,
        mode='lines',
        name='Islas Baleares',
        marker=dict(color='rgba(0, 0, 102, 0.8)'))

    # Creating trace17. creamos 17 línea
    trace17 = go.Scatter(
        x=dfAS.fecha,
        y=dfAS.num_casos,
        mode='lines',
        name='Principado de Asturias',
        marker=dict(color='rgba(0, 102, 0, 0.8)'))

    # Creating trace18. creamos 18 línea
    trace18 = go.Scatter(
        x=dfCB.fecha,
        y=dfCB.num_casos,
        mode='lines',
        name='Cantabria',
        marker=dict(color='rgba(255, 51, 255, 0.8)'))

    # Creating trace19. creamos 19 línea
    trace19 = go.Scatter(
        x=dfGA.fecha,
        y=dfGA.num_casos,
        mode='lines',
        name='Galicia',
        marker=dict(color='rgba(128, 128, 128, 0.8)'))

    # Creating trace20. creamos 20 línea
    trace20 = go.Scatter(
        x=dfCN.fecha,
        y=dfCN.num_casos,
        mode='lines',
        name='Canarias',
        marker=dict(color='rgba(203, 95, 0, 0.8)'))

    layout = dict(xaxis=dict(title='fecha', ticklen=5), height=700, width=1200)

    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12,
            trace13, trace14, trace15, trace16, trace17, trace18, trace19, trace20]

    graph_sit_ccaa1 = go.Figure(dict(data=data,
                         layout=layout))

    return graph_sit_ccaa1

df6 = pd.read_csv('data/df_merge_ccaa2.csv')

def graph_inc_acum(df6):

    # Ordeno de menor a mayor por la columna 'incidencia acumulada a 14 días'
    df_merge_ccaa2_mayor = df6.sort_values(['incidencia acumulada a 14 días'])

    '''
    Gráfica de la incidencia acumulada del COVID-19 en los últimos 14 y 7 días para cada CCAA y 100.000 habitantes
    '''
    x = df_merge_ccaa2_mayor.comunidad

    trace1 = {
        'x': x,
        'y': df_merge_ccaa2_mayor['incidencia acumulada a 14 días'],
        'name': '14 días',
        'type': 'bar'
    }

    trace2 = {
        'x': x,
        'y': df_merge_ccaa2_mayor['incidencia acumulada a 7 días'],
        'name': '7 días',
        'type': 'bar'
    }

    data = [trace1, trace2]
    layout = {'height': 600, 'width': 730,
#        'title': 'Incidencia acumulada CCAA',
        'xaxis': {'title': 'CCAA'}
    }

    graph_inc_acum = go.Figure(data=data, layout=layout)
    graph_inc_acum.update_xaxes(
            tickangle= 45
            )

    return graph_inc_acum

def graph_map_acum(df6):
    '''
    Genero un nuevo DataFrame para realizar los mapas con Folium
    IA COVID-19 en los últimos 14 días por CCAA
    '''

    # Añado el cod_ccaa a cada comunidad autónoma
    df6['ccaa'] = ['01', '02', '04', '05', '07', '06', '08', '09', '16', '19', '13', '17', '10', '11', '03', '12',
                       '14', '18', '15']

    # Cargo el json
    with open('data/spain_provinces.geojson', "r", encoding="utf-8") as response:
        geojson_espana = json.load(response)

    # Inicializo el mapa
    mapa = folium.Map(location=[40, -5], zoom_start=5, tiles='cartodbpositron')

    # Añado el color al chloropleth
    choropleth = folium.Choropleth(
    geo_data=geojson_espana,
    name='choropleth',
    data=df6,
    columns=['ccaa', 'incidencia acumulada a 14 días'],
    key_on='feature.properties.region',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='IA 14 días CCAA (casos/100.000 habitantes)',
    highlight=True,
    smooth_factor = 0).add_to(mapa)

    style_function = "font-size: 15px; font-weight: bold"
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['name'], style=style_function, labels=False))

    #color
    tiles = ['stamenwatercolor','openstreetmap','stamenterrain']

    for tile in tiles:
        folium.TileLayer(tile).add_to(mapa)

    folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(mapa)
    folium.TileLayer('cartodbpositron',name="light mode",control=True).add_to(mapa)
    folium.LayerControl().add_to(mapa)

    return mapa

def graph_map1_acum(df6):
    '''
    Genero un nuevo DataFrame para realizar los mapas con Folium
    IA COVID-19 en los últimos 7 días por CCAA
    '''

    # Añado el cod_ccaa a cada comunidad autónoma
    df6['ccaa'] = ['01', '02', '04', '05', '07', '06', '08', '09', '16', '19', '13', '17', '10', '11', '03', '12',
                       '14', '18', '15']

    # Cargo el json
    with open('data/spain_provinces.geojson', "r", encoding="utf-8") as response:
        geojson_espana = json.load(response)

    # Inicializo el mapa
    mapa = folium.Map(location=[40, -5], zoom_start=5, tiles='cartodbpositron')

    # Añado el color al chloropleth
    choropleth = folium.Choropleth(
    geo_data=geojson_espana,
    name='choropleth',
    data=df6,
    columns=['ccaa', 'incidencia acumulada a 7 días'],
    key_on='feature.properties.region',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='IA 7 días CCAA (casos/100.000 habitantes)',
    highlight=True,
    smooth_factor = 0).add_to(mapa)

    style_function = "font-size: 15px; font-weight: bold"
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['name'], style=style_function, labels=False))

    #color
    tiles = ['stamenwatercolor','openstreetmap','stamenterrain']

    for tile in tiles:
        folium.TileLayer(tile).add_to(mapa)

    folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(mapa)
    folium.TileLayer('cartodbpositron',name="light mode",control=True).add_to(mapa)
    folium.LayerControl().add_to(mapa)

    return mapa

df7 = pd.read_csv('data/casos_def1.csv')

def graph_def_num(df7):
    # Ordeno de menor a mayor por la columna 'número de defunciones a 14 días'
    casos_def2_mayor = df7.sort_values(['número de defunciones a 14 días'])

    '''
    Gráfica de defunciones del COVID-19 en los últimos 14 y 7 días para cada CCAA
    '''
    x = casos_def2_mayor.comunidad

    trace1 = {
        'x': x,
        'y': casos_def2_mayor['número de defunciones a 14 días'],
        'name': '14 días',
        'type': 'bar'
    }

    trace2 = {
        'x': x,
        'y': casos_def2_mayor['número de defunciones a 7 días'],
        'name': '7 días',
        'type': 'bar'
    }

    data = [trace1, trace2]
    layout = {'height': 600, 'width': 730,
#        'title': 'Número de defunciones últimos días CCAA',
        'xaxis': {'title': 'CCAA'}
    }

    graph_def_num = go.Figure(data=data, layout=layout)
    graph_def_num.update_xaxes(
            tickangle= 45
            )

    return graph_def_num



