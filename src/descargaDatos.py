import krakenex
from pykrakenapi import KrakenAPI

def descargar_datos(par):
    api = krakenex.API()
    k = KrakenAPI(api)
    ohlc, last = k.get_ohlc_data(par)
    #print(ohlc.head)
def menu_seleccion_par():
    pares = {
        1 : "BTC/USD",
        2 : "ETH/USD",
        3 : "USDT/USD",
        4 : "XRP/USD",
        5 : "USDC/USD",
        6 : "SOL/USD",
        7 : "ADA/USD",
        8 : "DOGE/USD",
        9 : "TRX/USD",
        10 : "LINK/USD",
        11 : "SALIR"
    }

    while True:
        print("Seleccione un par de monedas:")
        for key, value in pares.items():
            print(f"{key}. {value}")

        opcion = int(input("Introduzca el número de la opción deseada:"))

        if opcion == 5:
            print("SALIENDO")
            break
        elif opcion in range (1,10):
            descargar_datos(pares.get(opcion))
            break
        else:
            print("Selección no válida")


if __name__ == "__main__":
    menu_seleccion_par()