import krakenex
import pandas as pd
from pykrakenapi import KrakenAPI

class DescargadorDatos:
    def __init__(self):
        self.api = krakenex.API()
        self.kraken_api = KrakenAPI(self.api)
    def descargar_datos(self, par, intervalo=10080): #Semanal, 10080 minutos en una semana; diario 1440
        ohlc, last = self.kraken_api.get_ohlc_data(par,intervalo,ascending = True)
        return ohlc

if __name__ == "__main__":
    descargador = DescargadorDatos()
    datos = descargador.descargar_datos("ETHUSD")
