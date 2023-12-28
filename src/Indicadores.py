import pandas as pd
import matplotlib.pyplot as plt
import DescargadorDatos as dd
import mplfinance as mpf

class Indicadores:

    def __init__(self, datos):
        try:
            if not isinstance(datos, pd.DataFrame):
                raise ValueError("Los datos deben ser un DataFrame de pandas.")

            # Resto del código para la inicialización
            since = input("¿Desde qué fecha quiere los datos? (YYYY-MM-DD): ")
            self.datos = datos.loc[since:,]
            self.datos = self.datos.dropna()
            self.datos = self.datos.drop('time', axis=1)
            self.datos = self.datos.drop('vwap', axis=1)
            self.datos['open'] = pd.to_numeric(self.datos['open'], errors='coerce')
            self.datos['high'] = pd.to_numeric(self.datos['high'], errors='coerce')
            self.datos['low'] = pd.to_numeric(self.datos['low'], errors='coerce')
            self.datos['close'] = pd.to_numeric(self.datos['close'], errors='coerce')
            self.datos['volume'] = pd.to_numeric(self.datos['volume'], errors='coerce')
            self.datos = self.datos.rename(columns={
                'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume','count': 'Count'})

        except Exception as e:
            print(f"Error durante la inicialización: {e}")

    def calcular_estocastico(self, periodos=14, k_suavizado=3, d_suavizado=3):
        # Calcular %K
        self.datos['Min'] = self.datos['Low'].rolling(window=periodos, min_periods=1).min() #Calcula minimo
        self.datos['Max'] = self.datos['High'].rolling(window=periodos, min_periods=1).max() #Calcula máximo

        self.datos['%K'] = ((self.datos['Close'] - self.datos['Min']) / (self.datos['Max'] - self.datos['Min'])) * 100

        # Calcular %D (Suavizado de %K)
        self.datos['%D'] = self.datos['%K'].rolling(window=k_suavizado, min_periods=1).mean()

        # Calcular %SD (Suavizado de %D)
        self.datos['%SD'] = self.datos['%D'].rolling(window=d_suavizado, min_periods=1).mean()

    def graficar_estocastico(self):
        # Gráfico de %K y %D
        addplt = [
            mpf.make_addplot(self.datos['%K'], label='%K', color='red', panel = 2),
            mpf.make_addplot(self.datos['%D'], label='%D', color='green', panel = 2),
        ]
        fig1, axlist = mpf.plot(
            self.datos, type = 'candle',style='yahoo', volume = True, title = 'GRÁFICO DE VELAS',
            ylabel = 'PRECIO',ylabel_lower = 'VOLUMEN', figsize =(18,10), addplot = addplt
        )
        fig1.suptitle('GRÁFICO DE VELAS', fontsize = 25, loc = 'center')
        plt.show()

        # Mostrar leyendas
        fig.tight_layout()
        print('OK 10')
        fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
        print('OK 11')

    def calcular_ordenes(self):
        #Condiciones de compra. Cuando %K (linea azul) cruza a %D (linea roja) hacia arriba.
        condiciones_compra = ((self.datos['%K'] > self.datos['%D']) &
                              (self.datos['%K'].shift(1) <= self.datos['%D'].shift(1)))
        condiciones_venta = ((self.datos['%K'] < self.datos['%D']) &
                              (self.datos['%K'].shift(1) >= self.datos['%D'].shift(1)))

        #Asigna un 1 cuando la orden es de compra y un -1 cuando es de venta, deja un 0 cuando hay que mantener.
        self.datos['Orden'] = 0
        self.datos.loc[condiciones_compra, 'Orden'] = 1 #Compra
        self.datos.loc[condiciones_venta, 'Orden'] = -1 #Venta

    def graficar_ordenes(self):
        plt.figure(figsize=(10, 6))

        # Gráfico de precios
        plt.plot(self.datos['Close'], label='Precio de cierre', color='blue')

        # Marcadores para órdenes de compra y venta
        add1 = mpf.make_addplot(self.datos.index[self.datos['Orden'] == 1],
                         self.datos['Close'][self.datos['Orden'] == 1],
                         marker='^', color='green', label='Compra', lw=0, s=100, type='scatter', panel=2)

        mpf.plt(self.datos.index[self.datos['Orden'] == -1],
                         self.datos['close'][self.datos['Orden'] == -1],
                         marker='v', color='red', label='Venta', lw=0, s=100, type='scatter', panel=2, addplot = add1 )

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
            print(datos)
            indicadores = Indicadores(datos)
            indicadores.calcular_estocastico()
            indicadores.graficar_estocastico()
            indicadores.calcular_ordenes()
            indicadores.graficar_ordenes()

        else:
            print("No se pudieron obtener los datos.")

    except Exception as e:
        print(f"Error general: {e}")

