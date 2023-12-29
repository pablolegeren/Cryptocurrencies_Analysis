import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

class Graficos:

    def __init__(self, datos):
        self.datos = datos

    def graficar_datos(self):
        # Gráfico de velas con Plotly
        st.header("Gráfico de Velas")
        fig = go.Figure(data=[go.Candlestick(x=self.datos.index,
                                             open=self.datos['open'],
                                             high=self.datos['high'],
                                             low=self.datos['low'],
                                             close=self.datos['close'])])
        st.plotly_chart(fig)

    def graficar_estocastico(self):
        # Gráfico de %K y %D
        st.header("Gráfico de Estocástico")
        st.line_chart(self.datos[['%K', '%D']])

    def graficar_ordenes(self):
        fig = px.line(x=self.datos.index, y=self.datos['close'], labels={'y': 'Precio de cierre'},
                      title='Órdenes de Compra y Venta')

        compras = self.datos[self.datos['Orden'] == 1]
        ventas = self.datos[self.datos['Orden'] == -1]

        fig.add_trace(go.Scatter(x=compras.index, y=compras['close'], mode='markers', name='Compra',
                                 marker=dict(color='green', size=10)))
        fig.add_trace(go.Scatter(x=ventas.index, y=ventas['close'], mode='markers', name='Venta',
                                 marker=dict(color='red', size=10)))

        # Mostrar gráfico
        st.plotly_chart(fig)
