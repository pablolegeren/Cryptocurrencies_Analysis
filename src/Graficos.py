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
        st.header("Indicadores Estocásticos")
        fig_estocastico = go.Figure()

        fig_estocastico.add_trace(go.Scatter(x=self.datos.index, y=self.datos['%K'], mode='lines', name='%K'))
        fig_estocastico.add_trace(go.Scatter(x=self.datos.index, y=self.datos['%D'], mode='lines', name='%D'))

        # Configura el diseño del gráfico
        fig_estocastico.update_layout(
            xaxis_title="Fecha",
            yaxis_title="Valor",
            legend=dict(title="Indicadores"),
        )

        # Muestra el gráfico de Plotly
        st.plotly_chart(fig_estocastico, use_container_width=True, width=0)

    def graficar_ordenes(self):
        st.header("Ordenes de compra y venta")
        fig = px.line(x=self.datos.index, y=self.datos['close'], labels={'x': 'Fecha', 'y': 'Precio de cierre'})

        compras = self.datos[self.datos['Orden'] == 1]
        ventas = self.datos[self.datos['Orden'] == -1]

        fig.add_trace(go.Scatter(x=compras.index, y=compras['close'], mode='markers', name='Compra',
                                 marker=dict(color='green', size=10)))
        fig.add_trace(go.Scatter(x=ventas.index, y=ventas['close'], mode='markers', name='Venta',
                                 marker=dict(color='red', size=10)))

        # Mostrar gráfico
        st.plotly_chart(fig)
