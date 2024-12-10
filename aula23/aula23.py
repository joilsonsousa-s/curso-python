class Carro:
    valMAx = 0
    ligado = True
    cor = ""

c1 = Carro()
c1.valMAx = 200
c1.ligado = True
c1.cor = "Preto"
print("Velocidade do carro: " + str(c1.valMAx))
estado = "Sim" if c1.ligado else "Não"
print("Carro liagado: " + str(estado))
print("Cor do carro: " + c1.cor)