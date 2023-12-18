from Menu import *
from DescargadorDatos import *
from Indicadores import *

def main():
    try:
        # Menu de selección
        menu = Menu()
        par = menu.menu()

        # Descarga de datos
        descargador = DescargadorDatos()
        datos = descargador.descargar_datos(par)

        if datos is not None:
            # Indicadores
            indicadores = Indicadores(datos)

            # Calcular y graficar estocásticos
            indicadores.calcular_estocastico()
            indicadores.graficar_estocastico()

            # Calcular y graficar órdenes
            indicadores.calcular_ordenes()
            indicadores.graficar_ordenes()

        else:
            print("No se pudieron obtener los datos.")

    except Exception as e:
        print(f"Error en la ejecución principal: {e}")

if __name__ == "__main__":
    main()
