num = "Joilson"

if not type(num) is int:
    raise Exception("Somente números permitidos!")
else:
    print(str(num))

"""
num = -10

if num < 1:
    raise Exception("Valor não é permitido!")
"""

"""
x = 7

try:
    print(x)
except:
    print("Erro no programa.")
else:
    print("Tudo certo.")
finally:
    print("Fim do programa.")
"""