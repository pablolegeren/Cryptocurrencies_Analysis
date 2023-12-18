import pandas as pd
import matplotlib.pyplot as plt
import DescargadorDatos as dd

class Indicadores:

    def __init__(self, datos):
        try:
            if not isinstance(datos, pd.DataFrame):
                raise ValueError("Los datos deben ser un DataFrame de pandas.")

            # Resto del código para la inicialización
            self.datos = datos

        except Exception as e:
            print(f"Error durante la inicialización: {e}")

    def calcular_estocastico(self, periodos=14, k_suavizado=3, d_suavizado=3):
        # Calcular %K
        self.datos['min'] = self.datos['low'].rolling(window=periodos, min_periods=1).min()
        self.datos['max'] = self.datos['high'].rolling(window=periodos, min_periods=1).max()
        self.datos['%K'] = ((self.datos['close'] - self.datos['min']) / (self.datos['max'] - self.datos['min'])) * 100

        # Calcular %D (Suavizado de %K)
        self.datos['%D'] = self.datos['%K'].rolling(window=k_suavizado, min_periods=1).mean()

        # Calcular %SD (Suavizado de %D)
        self.datos['%SD'] = self.datos['%D'].rolling(window=d_suavizado, min_periods=1).mean()

    def graficar_estocastico(self):
        self.datos=self.datos.head(60)
        fig, ax1 = plt.subplots(figsize=(10, 6))

        # Gráfico de precios
        ax1.plot(self.datos['close'], label='Precio de cierre', color='blue')
        ax1.set_xlabel('Fecha')
        ax1.set_ylabel('Precio de cierre', color='blue')
        ax1.tick_params('y', colors='blue')

        # Gráfico de %K y %D
        ax2 = ax1.twinx()
        ax2.plot(self.datos['%K'], label='%K', color='green')
        ax2.plot(self.datos['%D'], label='%D', linestyle='dashed', color='red')
        ax2.set_ylabel('%K / %D', color='green')
        ax2.tick_params('y', colors='green')

        # Mostrar leyendas
        fig.tight_layout()
        fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

        # Mostrar el gráfico
        plt.title('Gráfico de Estocástico')
        plt.show()

    def calcular_ordenes(self):
        #Condiciones de compra. Cuando %K (linea azul) cruza a %D (linea roja) hacia arriba.
        condiciones_compra = ((self.datos['%K'] > self.datos['%D']) &
                              (self.datos['%K'].shift(1) <= self.datos['%D'].shift(1)))
        condiciones_venta = ((self.datos['%K'] < self.datos['%D']) &
                              (self.datos['%K'].shift(1) >= self.datos['%D'].shift(1)))

        #Asigna un 1 cuando la orden es de compra y un -1 cuando es de venta, deja un 0 cuando hay que mantener.
        self.datos['orden'] = 0
        self.datos.loc[condiciones_compra, 'orden'] = 1 #Compra
        self.datos.loc[condiciones_venta, 'orden'] = -1 #Venta

    def graficar_ordenes(self):
        plt.figure(figsize=(10, 6))

        # Gráfico de precios
        plt.plot(self.datos['close'], label='Precio de cierre', color='blue')

        # Marcadores para órdenes de compra y venta
        plt.scatter(self.datos.index[self.datos['orden'] == 1],
                    self.datos['close'][self.datos['orden'] == 1],
                    marker='^', color='green', label='Compra', lw=0, s=100)

        plt.scatter(self.datos.index[self.datos['orden'] == -1],
                    self.datos['close'][self.datos['orden'] == -1],
                    marker='v', color='red', label='Venta', lw=0, s=100)

        # Configuración del gráfico
        plt.xlabel('Fecha')
        plt.ylabel('Precio de cierre')
        plt.title('Órdenes de Compra y Venta')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    try:
        descargador = dd.DescargadorDatos()
        datos = descargador.descargar_datos("BTCUSD")

        if datos is not None:
            indicadores = Indicadores(datos)
            indicadores.calcular_estocastico()
            indicadores.graficar_estocastico()
            indicadores.calcular_ordenes()
            indicadores.graficar_ordenes()
        else:
            print("No se pudieron obtener los datos.")

    except Exception as e:
        print(f"Error general: {e}")


if __name__ == "__main__":
    descargador = dd.DescargadorDatos()
    datos = descargador.descargar_datos("BTCUSD")
    indicadores = Indicadores(datos)
    indicadores.calcular_estocastico()
    indicadores.graficar_estocastico()
    indicadores.calcular_ordenes()
    indicadores.graficar_ordenes()

