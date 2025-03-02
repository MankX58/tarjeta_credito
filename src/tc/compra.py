
from src.tc import get_tasa_usura_mv
from src.tc.cuota import Cuota


class Compra:
    def __init__(self, tasa:float, valor:float, cuotas:int):
       self.set_tasa(tasa)
       self.set_valor(valor)
       self.set_numero_cuotas(cuotas)
       self.__cuotas:list[Cuota] = []

    def get_tasa(self)->float:
        return self.__tasa
    
    def set_tasa(self,tasa:float):
        tasa_usura = get_tasa_usura_mv()
        if(tasa>tasa_usura):
            raise Exception(f"La tasa {tasa} es mayor a la tasa de usura permitida {tasa_usura}")
        self.__tasa = tasa
    
    def set_valor(self,valor:float):
        if valor <= 0:
            raise Exception(f"El valor de la compra {valor} debe ser mayor a cero")
        self.__valor = valor

    def get_valor(self)->float:
        return self.__valor

    def set_numero_cuotas(self,cuotas:int):
        if cuotas <= 0:
            raise Exception(f"El número de cuotas {cuotas} debe ser mayor a cero ")
        self.__numero_cuotas = cuotas

    def get_numero_cuotas(self)->int:
        return self.__numero_cuotas
    
    def calcular_cuota(self)->float:
        if(self.__tasa == 0):
            return self.__valor/self.__numero_cuotas
        if(self.__numero_cuotas == 1):
            return self.__valor
        
        return (self.__valor*self.__tasa)/(1-(1+self.__tasa)**(-self.__numero_cuotas))
    
    def calcular_intereses(self)->float:
        if self.__tasa ==0:
            return 0
        if self.__numero_cuotas ==1:
            return 0
        return (self.calcular_cuota()*self.__numero_cuotas)-self.__valor
    
    
    def calcular_plan_amortizacion(self)->list[Cuota]:
        plan:list[Cuota] = []
        valor_cuota = self.calcular_cuota()
        if self.__numero_cuotas ==1:
            cuota_i = Cuota(1,valor_cuota, valor_cuota, 0)
            plan.append(cuota_i)
            return plan
        
        saldo = self.__valor 
        for i in range(self.__numero_cuotas):
            AI = saldo*self.__tasa
            AC = valor_cuota - AI
            cuota_i = Cuota(i+1,valor_cuota, AC, AI)
            plan.append(cuota_i)
            saldo = saldo - AC
        return plan
        
            



        
        
