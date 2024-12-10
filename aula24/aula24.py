class Carro:
    valMAx = 0
    ligado = True
    cor = ""

    def __init__(self,v,l,c):
        self.valMAx = v
        self.ligado = l
        self.cor = c

    def mostrar(self):
        print("Velocidade máxima: " + str(self.valMAx))
        estado = "Sim" if self.ligado else "Não"
        print("Ligado: " + str(estado))
        print("O carro está: " + self.andar())
        print("Cor: " + self.cor)
        print("--------------------------")

    def ligar(self):
        self.ligado = True

    def desligado(self):
        self.ligado = False

    def andar(self):
        if (self.ligado):
            return "Andando"
        else:
            return "Desligado"

c1 = Carro(200,True,"Preto")
c2 = Carro(150,True,"Branco")
c3 = Carro(0,False,"Verde")

c1.desligado()

c1.mostrar()
c2.mostrar()
c3.mostrar()