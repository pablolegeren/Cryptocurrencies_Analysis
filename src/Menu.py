from DescargadorDatos import DescargadorDatos

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
            11: "SALIR"
        }


    def menu(self):
        while True:
            print("Seleccione un par de monedas:")
            for key, value in self.pares.items():
                print(f"{key}. {value}")

            opcion = int(input("Introduzca el par deseado: "))

            if opcion == 11:
                print("SALIENDO")
                break
            elif opcion in range(1, 11):
                return self.pares[opcion]
            else:
                print("Selección no válida")



    def descargar_y_procesar_datos(self, par):
        datos = self.descargador.descargar_datos(par)
        print(f"Datos descargados para {par}:\n{datos.head()}")
