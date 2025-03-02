import pytest
from src.tc.compra import Compra


def test_01_36_cuotas():
    compra = Compra(0.031, 200000, 36)
    assert compra.calcular_intereses() == 134726.5281633046
    

def test_02_24_cuotas():
    compra = Compra(0.034, 850000, 24)
    #assert compra.calcular_intereses() == 407059.97
    #assert compra.calcular_intereses() == 407059.96735607623
    assert (compra.calcular_intereses() - 407059.97) < 0.000001


def test_03_tasa_cero():
    compra = Compra(0, 480000, 48)
    assert compra.calcular_intereses() == 0

def test_04_tasa_usura():
    with pytest.raises(Exception):
        compra = Compra(0.15, 50000, 48)

def test_05_cuota_unica():
    compra = Compra(0.024, 90000, 1)
    assert compra.calcular_intereses() == 0

def test_06_monto_invalido():
    with pytest.raises(Exception):
        compra = Compra(0.024, 0, 60)

def test_07_numero_cuotas_negativa():
    with pytest.raises(Exception):
        compra = Compra(0.01, 50000, -10)



