#TASA_USURA_EA = 0.2489
TASA_USURA_EA = 4
#Hola

def get_tasa_usura_mv():
    return (1+TASA_USURA_EA)**(1/12)-1

def get_tasa_ea(tasa_mv):
    return ((1 + tasa_mv) **12)-1