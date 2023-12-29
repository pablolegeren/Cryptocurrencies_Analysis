# En tu aplicación principal (main.py)

from Menu import Menu
from DescargadorDatos import DescargadorDatos
from Indicadores import Indicadores
from Graficos import Graficos
import streamlit as st

def main():
    try:
        st.title("Análisis Técnico de Criptomonedas")

        # Menú de selección
        menu = Menu()
        par = menu.menu()

        # Descarga de datos
        descargador = DescargadorDatos()
        datos = descargador.descargar_datos(par)

        if datos is not None:

            # Indicadores
            indicadores = Indicadores(datos)

            # Calcular indicadores
            indicadores.calcular_estocastico()
            indicadores.calcular_ordenes()

            # Graficos
            graficos = Graficos(datos)
            graficos.graficar_datos()
            graficos.graficar_estocastico()
            graficos.graficar_ordenes()

        else:
            st.warning("No se pudieron obtener los datos.")

    except Exception as e:
        st.error(f"Error en la ejecución principal: {e}")

if __name__ == "__main__":
    main()
