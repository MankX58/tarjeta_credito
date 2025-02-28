from src.tc import compra


def test_caso01_36_cuotas():
    compra1 = compra.Compra(0.031, 200000, 36)
    assert compra1.calcular_intereses() == 134726.5281633046
    

def test_caso02_24_cuotas():
    compra2 = compra.Compra(0.034, 850000, 24)
    #assert compra2.calcular_intereses() == 407059.97
    #assert compra2.calcular_intereses() == 407059.96735607623
    assert (compra2.calcular_intereses() - 407059.97) < 0.000001


