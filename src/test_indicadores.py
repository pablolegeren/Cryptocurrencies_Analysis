import pandas as pd
from Indicadores import Indicadores

def test_calcular_estocastico():
    # Datos de prueba
    datos_prueba = pd.DataFrame({
        'open': [100, 110, 95, 105, 98, 105, 110, 120, 115, 105],
        'high': [120, 115, 100, 110, 102, 110, 115, 130, 120, 110],
        'low': [98, 105, 85, 95, 92, 95, 100, 110, 105, 95],
        'close': [105, 100, 90, 100, 95, 105, 105, 125, 110, 100]
    })

    # Crear instancia de Indicadores y calcular estocástico
    indicadores = Indicadores(datos_prueba)
    indicadores.calcular_estocastico(periodos=2)

    # Verificar que las columnas se hayan calculado correctamente
    assert 'Min' in datos_prueba.columns
    assert 'Max' in datos_prueba.columns
    assert '%K' in datos_prueba.columns
    assert '%D' in datos_prueba.columns
    assert '%SD' in datos_prueba.columns

    # Verificar que los cálculos sean precisos (puedes ajustar las aserciones según tus necesidades)
    assert datos_prueba['Min'].iloc[0] == 98
    assert datos_prueba['Max'].iloc[0] == 120
    assert datos_prueba["%K"].iloc[0] == 7/22*100
    assert datos_prueba["%D"].iloc[0] == datos_prueba["%K"].iloc[0:1].mean()
    assert datos_prueba["%SD"].iloc[0] == datos_prueba["%D"].iloc[0:1].mean()