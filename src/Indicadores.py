import pandas as pd
import matplotlib.pyplot as plt
import DescargadorDatos as dd

class Indicadores:

    def __init__(self, datos):
        self.datos=datos

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

    def generar_senales(self):
        # Generar señales de compra y venta según las condiciones del estocástico
        self.datos.loc[:, 'senyal'] = 0  # 0: Mantener, 1: Comprar, -1: Vender

        # Condiciones de sobrecompra y sobreventa
        sobrecompra_condicion = self.datos['%K'] > 80
        sobreventa_condicion = self.datos['%K'] < 20

        # Generar señales de compra y venta
        self.datos.loc[sobrecompra_condicion & (self.datos['%D'] > self.datos['%K']), 'senyal'] = -1  # Vender
        self.datos.loc[sobreventa_condicion & (self.datos['%D'] < self.datos['%K']), 'senyal'] = 1  # Comprar

        # Eliminar filas con señal 0 (mantener) para mejorar la visualización del gráfico
        self.datos = self.datos[self.datos['senyal'] != 0]

    def graficar_senales(self):
        # Gráfico de señales de compra y venta
        plt.figure(figsize=(10, 6))
        plt.plot(self.datos['close'], label='Precio de cierre', color='blue')
        plt.scatter(self.datos.index, self.datos['senyal'] * self.datos['close'], marker='^', color='green',
                    label='Compra', lw=0, s=100)
        plt.scatter(self.datos.index, -self.datos['senyal'] * self.datos['close'], marker='v', color='red',
                    label='Venta', lw=0, s=100)
        plt.xlabel('Fecha')
        plt.ylabel('Precio de cierre')
        plt.title('Señales de Compra y Venta')
        plt.legend()
        plt.show()
        #TODO Arreglar, no funciona bien

if __name__ == "__main__":
    descargador = dd.DescargadorDatos()
    datos = descargador.descargar_datos("BTCUSD")
    indicadores = Indicadores(datos)
    indicadores.calcular_estocastico()
    indicadores.graficar_estocastico()