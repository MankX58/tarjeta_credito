from src.tc.compra import Compra
from src.tc.cuota import Cuota
from src.tc import get_tasa_ea, get_tasa_usura_mv 
from src.tc import TASA_USURA_EA
 
tasa_usura = get_tasa_usura_mv()
print("usura efectiva anual", TASA_USURA_EA*100, "%" )
print("usura mensual vencido", tasa_usura*100, "%" )
print(get_tasa_ea(0.13)*100)

PRESICION = 0.001
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
print (plan)
for i in range(len(plan_esperado)):
    print (f"{plan_esperado[i] } == {plan[i]} es igual {plan_esperado[i]==plan[i]}")
    