def somar(*num):
    r = 0
    for n in num:
        r += n
    print("A soma: "+str(r))
    
somar(3,4,70,7)

"""
valores = [3,4,70,7]
def somar(num):
    r = 0
    for n in num:
        r += n
    print("A soma: "+str(r))
somar(valores)
"""

"""
def carros(c="Ford"):
    print("Modelo " + c)
carros()
"""