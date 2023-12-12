from Menu import *
from DescargadorDatos import *
from Indicadores import *

def main():
    #Menu de selección
    menu = Menu()
    par = menu.menu()

    #Descarga de datos
    descargador = DescargadorDatos()
    datos = descargador.descargar_datos(par)

    #Indicadores
    indicadores = Indicadores(datos)

    #Calcular y graficar estocásticos
    indicadores.calcular_estocastico()
    indicadores.graficar_estocastico()

    #Calcular y graficar odenes
    #indicadores.generar_senales()
    #indicadores.graficar_senales()

if __name__ == "__main__":
    main()
