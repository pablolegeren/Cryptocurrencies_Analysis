from src.Menu import Menu
from src.DescargadorDatos import DescargadorDatos
from src.Indicadores import Indicadores
from unittest.mock import patch

def test_integration():
    with patch.object(Menu, 'menu', return_value="BTC/USD"):
        menu = Menu()
        par = menu.menu()
        assert par == "BTC/USD"

        descargador = DescargadorDatos()
        datos = descargador.descargar_datos(par)
        assert datos is not None

        indicadores = Indicadores(datos)
        indicadores.calcular_estocastico()
        indicadores.calcular_ordenes()

        verificar = ["%K", "%D", "%SD", "Orden"]
        for v in verificar:
            assert datos[v].notna().all()
