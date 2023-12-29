
from DescargadorDatos import DescargadorDatos
# Añade la siguiente importación al principio del archivo
import streamlit as st


class Menu:
    def __init__(self):
        self.descargador = DescargadorDatos()
        self.pares = {
            1: "BTC/USD",
            2: "ETH/USD",
            3: "USDT/USD",
            4: "XRP/USD",
            5: "USDC/USD",
            6: "SOL/USD",
            7: "ADA/USD",
            8: "DOGE/USD",
            9: "TRX/USD",
            10: "LINK/USD",
        }

    def menu(self):
        st.sidebar.header("Selección de Par")

        # Selección de par de monedas
        opcion_par = st.sidebar.selectbox("Seleccione un par de monedas:", list(self.pares.values()))

        return opcion_par


