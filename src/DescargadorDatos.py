import krakenex
import pandas as pd
from pykrakenapi import KrakenAPI

class DescargadorDatos:
    def __init__(self):
        self.api = krakenex.API()
        self.kraken_api = KrakenAPI(self.api)

    def descargar_datos(self, par):
        try:
            ohlc, last = self.kraken_api.get_ohlc_data(par, ascending=True)
            ohlc = pd.DataFrame(ohlc)
            ohlc[['open', 'high', 'low', 'close']] = ohlc[['open', 'high', 'low', 'close']].astype(float)
            ohlc["time"] = pd.to_datetime(ohlc["time"], unit="s")
            return ohlc
        except Exception as e:
            print(f"Error al descargar datos: {e}")
            return None
