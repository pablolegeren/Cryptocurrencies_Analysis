import krakenex
from pykrakenapi import KrakenAPI

class DescargadorDatos:
    def __init__(self):
        self.api = krakenex.API()
        self.kraken_api = KrakenAPI(self.api)

    def descargar_datos(self, par):
        ohlc, last = self.kraken_api.get_ohlc_data(par)
        return ohlc
