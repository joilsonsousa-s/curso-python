valores = [50,20,7]
def somar(num):
    r = 0
    for n in num:
        r += n
    return r

def valList(num):
    lista = []
    for v in num:
        lista.append(v)
    return lista
print("Valores: " +str(valList(valores))+ " soma: "+ str(somar(valores)))