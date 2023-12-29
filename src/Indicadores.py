import pandas as pd

class Indicadores:

    def __init__(self, datos):
        self.datos = datos

    def calcular_estocastico(self, periodos=14, k_suavizado=3, d_suavizado=3):
        # Cálculo de %K
        self.datos['Min'] = self.datos['low'].rolling(window=periodos, min_periods=1).min()
        self.datos['Max'] = self.datos['high'].rolling(window=periodos, min_periods=1).max()
        self.datos['%K'] = ((self.datos['close'] - self.datos['Min']) / (self.datos['Max'] - self.datos['Min']).replace(0, 1)) * 100

        # Cálculo de %D (Suavizado de %K)
        self.datos['%D'] = self.datos['%K'].rolling(window=k_suavizado, min_periods=1).mean()

        # Cálculo de %SD (Suavizado de %D)
        self.datos['%SD'] = self.datos['%D'].rolling(window=d_suavizado, min_periods=1).mean()

    def calcular_ordenes(self):
        condiciones_compra = ((self.datos['%K'] > self.datos['%D']) &
                              (self.datos['%K'].shift(1) <= self.datos['%D'].shift(1)))
        condiciones_venta = ((self.datos['%K'] < self.datos['%D']) &
                              (self.datos['%K'].shift(1) >= self.datos['%D'].shift(1)))

        # Asigna un 1 cuando la orden es de compra y un -1 cuando es de venta, deja un 0 cuando hay que mantener.
        self.datos['Orden'] = 0
        self.datos.loc[condiciones_compra, 'Orden'] = 1  # Compra
        self.datos.loc[condiciones_venta, 'Orden'] = -1  # Venta
