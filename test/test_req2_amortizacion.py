import pytest
from src.tc.compra import Compra
from src.tc.cuota import Cuota

PRESICION = 0.01

def test_08_Cuota_unica():
    plan_esperado = [Cuota(1, 90000, 90000, 0)]
    compra = Compra(0.024, 90000, 1)
    plan = compra.calcular_plan_amortizacion()
    for i in range(len(plan_esperado)):
        assert plan_esperado[i].get_numero() == plan[i].get_numero()
        assert plan_esperado[i].get_valor() == plan[i].get_valor()
        assert plan_esperado[i].get_valor_capital() == plan[i].get_valor_capital()
        assert plan_esperado[i].get_valor_interes() == plan[i].get_valor_interes()
        

def test_09_36Cuotas():
    plan_esperado = [
        Cuota(1, 9297.96, 3097.96, 6200.00),
        Cuota(2, 9297.96,  3194.00,6103.96),
        Cuota(3, 9297.96,  3293.01,6004.95),
        Cuota(4, 9297.96,  3395.09,5902.87),
        Cuota(5, 9297.96,  3500.34,5797.62),
        Cuota(6, 9297.96,  3608.85,5689.11),
        Cuota(7, 9297.96,  3720.73,5577.23),
        Cuota(8, 9297.96,  3836.07,5461.89),
        Cuota(9, 9297.96,  3954.99,5342.97),
        Cuota(10, 9297.96, 4077.59, 5220.37),
        Cuota(11, 9297.96, 4204.00, 5093.96),
        Cuota(12, 9297.96, 4334.32, 4963.64),
        Cuota(13, 9297.96, 4468.68, 4829.27),
        Cuota(14, 9297.96, 4607.21, 4690.75),
        Cuota(15, 9297.96, 4750.04, 4547.92),
        Cuota(16, 9297.96, 4897.29, 4400.67),
        Cuota(17, 9297.96, 5049.10, 4248.85),
        Cuota(18, 9297.96, 5205.63, 4092.33),
        Cuota(19, 9297.96, 5367.00, 3930.96),
        Cuota(20, 9297.96, 5533.38, 3764.58),
        Cuota(21, 9297.96, 5704.91, 3593.05),
        Cuota(22, 9297.96, 5881.76, 3416.19),
        Cuota(23, 9297.96, 6064.10, 3233.86),
        Cuota(24, 9297.96, 6252.09, 3045.87),
        Cuota(25, 9297.96, 6445.90, 2852.06),
        Cuota(26, 9297.96, 6645.72, 2652.23),
        Cuota(27, 9297.96, 6851.74, 2446.22),
        Cuota(28, 9297.96, 7064.15, 2233.81),
        Cuota(29, 9297.96, 7283.13, 2014.82),
        Cuota(30, 9297.96, 7508.91, 1789.05),
        Cuota(31, 9297.96, 7741.69, 1556.27),
        Cuota(32, 9297.96, 7981.68, 1316.28),
        Cuota(33, 9297.96, 8229.11, 1068.85),
        Cuota(34, 9297.96, 8484.21, 813.74),
        Cuota(35, 9297.96, 8747.23, 550.73),
        Cuota(36, 9297.96, 9018.39, 279.57)
    ]
    compra = Compra(0.031, 200000, 36)
    plan = compra.calcular_plan_amortizacion()
    for i in range(len(plan_esperado)):
        assert plan_esperado[i].get_numero() == plan[i].get_numero()
        assert abs(plan_esperado[i].get_valor() - plan[i].get_valor()) < PRESICION
        assert abs(plan_esperado[i].get_valor_capital() - plan[i].get_valor_capital()) < PRESICION
        assert abs(plan_esperado[i].get_valor_interes() - plan[i].get_valor_interes()) < PRESICION

def test_10_24Cuotas():
    plan_esperado = [
        Cuota(1, 52377.5, 23477.50, 28900.00),
        Cuota(2, 52377.5, 24275.73, 28101.77),
        Cuota(3, 52377.5, 25101.11, 27276.39),
        Cuota(4, 52377.5, 25954.55, 26422.95),
        Cuota(5, 52377.5, 26837.00, 25540.50),
        Cuota(6, 52377.5, 27749.46, 24628.04),
        Cuota(7, 52377.5, 28692.94, 23684.56),
        Cuota(8, 52377.5, 29668.50, 22709.00),
        Cuota(9, 52377.5, 30677.23, 21700.27),
        Cuota(10, 52377.5, 31720.26, 20657.24),
        Cuota(11, 52377.5, 32798.74, 19578.75),
        Cuota(12, 52377.5, 33913.90, 18463.60),
        Cuota(13, 52377.5, 35066.97, 17310.52),
        Cuota(14, 52377.5, 36259.25, 16118.25),
        Cuota(15, 52377.5, 37492.07, 14885.43),
        Cuota(16, 52377.5, 38766.80, 13610.70),
        Cuota(17, 52377.5, 40084.87, 12292.63),
        Cuota(18, 52377.5, 41447.75, 10929.75),
        Cuota(19, 52377.5, 42856.98, 9520.52),
        Cuota(20, 52377.5, 44314.11, 8063.39),
        Cuota(21, 52377.5, 45820.79, 6556.71),
        Cuota(22, 52377.5, 47378.70, 4998.80),
        Cuota(23, 52377.5, 48989.58, 3387.92),
        Cuota(24, 52377.5, 50655.22, 1722.28)
    ]
    compra = Compra(0.034, 850000, 24)
    plan = compra.calcular_plan_amortizacion()
    for i in range(len(plan_esperado)):
        assert plan_esperado[i].get_numero() == plan[i].get_numero()
        assert abs(plan_esperado[i].get_valor() - plan[i].get_valor()) < PRESICION
        assert abs(plan_esperado[i].get_valor_capital() - plan[i].get_valor_capital()) < PRESICION
        assert abs(plan_esperado[i].get_valor_interes() - plan[i].get_valor_interes()) < PRESICION

def test_11_TasaCero():
    plan_esperado = [
        Cuota(1,  10000.00, 10000.00, 0),
        Cuota(2,  10000.00, 10000.00, 0),
        Cuota(3,  10000.00, 10000.00, 0),
        Cuota(4,  10000.00, 10000.00, 0),
        Cuota(5,  10000.00, 10000.00, 0),
        Cuota(6,  10000.00, 10000.00, 0),
        Cuota(7,  10000.00, 10000.00, 0),
        Cuota(8,  10000.00, 10000.00, 0),
        Cuota(9,  10000.00, 10000.00, 0),
        Cuota(10, 10000.00, 10000.00, 0),
        Cuota(11, 10000.00, 10000.00, 0),
        Cuota(12, 10000.00, 10000.00, 0),
        Cuota(13, 10000.00, 10000.00, 0),
        Cuota(14, 10000.00, 10000.00, 0),
        Cuota(15, 10000.00, 10000.00, 0),
        Cuota(16, 10000.00, 10000.00, 0),
        Cuota(17, 10000.00, 10000.00, 0),
        Cuota(18, 10000.00, 10000.00, 0),
        Cuota(19, 10000.00, 10000.00, 0),
        Cuota(20, 10000.00, 10000.00, 0),
        Cuota(21, 10000.00, 10000.00, 0),
        Cuota(22, 10000.00, 10000.00, 0),
        Cuota(23, 10000.00, 10000.00, 0),
        Cuota(24, 10000.00, 10000.00, 0),
        Cuota(25, 10000.00, 10000.00, 0),
        Cuota(26, 10000.00, 10000.00, 0),
        Cuota(27, 10000.00, 10000.00, 0),
        Cuota(28, 10000.00, 10000.00, 0),
        Cuota(29, 10000.00, 10000.00, 0),
        Cuota(30, 10000.00, 10000.00, 0),
        Cuota(31, 10000.00, 10000.00, 0),
        Cuota(32, 10000.00, 10000.00, 0),
        Cuota(33, 10000.00, 10000.00, 0),
        Cuota(34, 10000.00, 10000.00, 0),
        Cuota(35, 10000.00, 10000.00, 0),
        Cuota(36, 10000.00, 10000.00, 0),
        Cuota(37, 10000.00, 10000.00, 0),
        Cuota(38, 10000.00, 10000.00, 0),
        Cuota(39, 10000.00, 10000.00, 0),
        Cuota(40, 10000.00, 10000.00, 0),
        Cuota(41, 10000.00, 10000.00, 0),
        Cuota(42, 10000.00, 10000.00, 0),
        Cuota(43, 10000.00, 10000.00, 0),
        Cuota(44, 10000.00, 10000.00, 0),
        Cuota(45, 10000.00, 10000.00, 0),
        Cuota(46, 10000.00, 10000.00, 0),
        Cuota(47, 10000.00, 10000.00, 0),
        Cuota(48, 10000.00, 10000.00, 0),
    ]
    compra = Compra(0, 480000, 48)
    plan = compra.calcular_plan_amortizacion()
    for i in range(len(plan_esperado)):
        assert plan_esperado[i].get_numero() == plan[i].get_numero()
        assert abs(plan_esperado[i].get_valor() - plan[i].get_valor()) < PRESICION
        assert abs(plan_esperado[i].get_valor_capital() - plan[i].get_valor_capital()) < PRESICION
        assert abs(plan_esperado[i].get_valor_interes() - plan[i].get_valor_interes()) < PRESICION

def test_12_TasaUsura():
    plan_esperado =  [
        Cuota(1,  6205.58, 5.58    , 6200.00),
        Cuota(2,  6205.58, 6.27    , 6199.31),
        Cuota(3,  6205.58, 7.05    , 6198.53),
        Cuota(4,  6205.58, 7.93    , 6197.66),
        Cuota(5,  6205.58, 8.91    , 6196.67),
        Cuota(6,  6205.58, 10.01   , 6195.57),
        Cuota(7,  6205.58, 11.26   , 6194.33),
        Cuota(8,  6205.58, 12.65   , 6192.93),
        Cuota(9,  6205.58, 14.22   , 6191.36),
        Cuota(10, 6205.58, 15.98   , 6189.60),
        Cuota(11, 6205.58, 17.97   , 6187.62),
        Cuota(12, 6205.58, 20.19   , 6185.39),
        Cuota(13, 6205.58, 22.70   , 6182.88),
        Cuota(14, 6205.58, 25.51   , 6180.07),
        Cuota(15, 6205.58, 28.68   , 6176.91),
        Cuota(16, 6205.58, 32.23   , 6173.35),
        Cuota(17, 6205.58, 36.23   , 6169.35),
        Cuota(18, 6205.58, 40.72   , 6164.86),
        Cuota(19, 6205.58, 45.77   , 6159.81),
        Cuota(20, 6205.58, 51.45   , 6154.13),
        Cuota(21, 6205.58, 57.83   , 6147.76),
        Cuota(22, 6205.58, 65.00   , 6140.58),
        Cuota(23, 6205.58, 73.06   , 6132.53),
        Cuota(24, 6205.58, 82.12   , 6123.47),
        Cuota(25, 6205.58, 92.30   , 6113.28),
        Cuota(26, 6205.58, 103.74  , 6101.84),
        Cuota(27, 6205.58, 116.61  , 6088.97),
        Cuota(28, 6205.58, 131.07  , 6074.51),
        Cuota(29, 6205.58, 147.32  , 6058.26),
        Cuota(30, 6205.58, 165.59  , 6039.99),
        Cuota(31, 6205.58, 186.12  , 6019.46),
        Cuota(32, 6205.58, 209.20  , 5996.38),
        Cuota(33, 6205.58, 235.14  , 5970.44),
        Cuota(34, 6205.58, 264.30  , 5941.29),
        Cuota(35, 6205.58, 297.07  , 5908.51),
        Cuota(36, 6205.58, 333.91  , 5871.68),
        Cuota(37, 6205.58, 375.31  , 5830.27),
        Cuota(38, 6205.58, 421.85  , 5783.73),
        Cuota(39, 6205.58, 474.16  , 5731.42),
        Cuota(40, 6205.58, 532.95  , 5672.63),
        Cuota(41, 6205.58, 599.04  , 5606.54),
        Cuota(42, 6205.58, 673.32  , 5532.26),
        Cuota(43, 6205.58, 756.81  , 5448.77),
        Cuota(44, 6205.58, 850.66  , 5354.92),
        Cuota(45, 6205.58, 956.14  , 5249.44),
        Cuota(46, 6205.58, 1074.70 , 5130.88),
        Cuota(47, 6205.58, 1207.96 , 4997.62),
        Cuota(48, 6205.58, 1357.75 , 4847.83),
        Cuota(49, 6205.58, 1526.11 , 4679.47),
        Cuota(50, 6205.58, 1715.35 , 4490.23),
        Cuota(51, 6205.58, 1928.06 , 4277.53),
        Cuota(52, 6205.58, 2167.13 , 4038.45),
        Cuota(53, 6205.58, 2435.86 , 3769.72),
        Cuota(54, 6205.58, 2737.90 , 3467.68),
        Cuota(55, 6205.58, 3077.41 , 3128.18),
        Cuota(56, 6205.58, 3459.00 , 2746.58),
        Cuota(57, 6205.58, 3887.92 , 2317.66),
        Cuota(58, 6205.58, 4370.02 , 1835.56),
        Cuota(59, 6205.58, 4911.9  , 1293.68),
        Cuota(60, 6205.58,  5520.98, 684.60 )
    ]
    compra = Compra(0.124, 50000, 60)
    plan = compra.calcular_plan_amortizacion()
    for i in range(len(plan_esperado)):
        assert plan_esperado[i].get_numero() == plan[i].get_numero()
        assert abs(plan_esperado[i].get_valor() - plan[i].get_valor()) < PRESICION
        assert abs(plan_esperado[i].get_valor_capital() - plan[i].get_valor_capital()) < PRESICION
        assert abs(plan_esperado[i].get_valor_interes() - plan[i].get_valor_interes()) < PRESICION

