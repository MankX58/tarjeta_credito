class Cuota:
    def __init__(self, numero:int, valor:float, valor_capital:float, valor_interes:float):
        self.__numero = numero
        self.__valor = valor
        self.__valor_capital = valor_capital 
        self.__valor_interes = valor_interes

    def get_numero(self)->int:
        return self.__numero
    
    def get_valor(self)->int:
        return self.__valor
    
    def get_valor_capital(self)->int:
        return self.__valor_capital
    
    def get_valor_interes(self)->int:
        return self.__valor_interes

    def __eq__(self, other: 'Cuota'):
        return (
            self.__numero == other.__numero 
            and self.__valor == other.__valor
            and self.__valor_capital == other.__valor_capital 
            and self.__valor_interes == other.__valor_interes
                )
    def __str__(self):
        return f"(num: {self.__numero} , valor: {self.__valor}, valor_capital: {self.__valor_capital} valor_interes: {self.__valor_interes})"