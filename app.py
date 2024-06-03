import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Anuncio de automóviles')

hist_checkbox = st.checkbox('Construir histograma')  # crear un checkbox

if hist_checkbox:  # al seleccionar el checkbox
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer", nbins=100)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox = st.checkbox(
    'Construir gráfico de dispersión')  # crear un checkbox

if scatter_checkbox:  # al seleccionar el checkbox
    # escribir un mensaje
    st.write('Creación de un grafico de dispersión mostrando el precio de acuerdo al combustible utilizado')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="price", y="fuel")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
