import os

carros = []

class Carro:
    nome = ""
    pot = 0
    velMax = 0
    ligado = False

    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot) * 2
        self.ligado = False

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False

    def info(self):
        print("Nome............: "+ self.nome)
        print("Potência........: "+ self.pot)
        print("Vel.Max.........: "+ self.velMax)
        print("Ligado..........: "+ "Sim" if self.ligado == True else "Não")

def Menu():
    os.system("cls") or None
    print("1 - Novo Carro")
    print("2 - Informações do Carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carro")
    print("7 - Sair")
    print("Quantidade de carros: "+ str(len(carros)))
    opc = input("Digite uma opção: ")
    return opc

def NovoCarro():
    os.system("cls") or None
    nome_car = input("Nome do Carro.....: ")
    pote_car = input("Potência do Carro.: ")
    car = Carro(nome_car, pote_car)
    carros.append(car)
    print("Novo carro Criado")
    os.system("pause")

def informacoes():
    os.system("cls") or None
    num_car = input("Informe o número do carro que deseja ver as informações: ")
    
    try:
        carros[int(num_car)].info()
    except:
        print("Carro não existe na lista")
    os.system("pause")


def ExcluirCarro():
    os.system("cls") or None
    num_car = input("Informe o número do carro que deseja excluir: ")
    
    try:
        del carros[int(num_car)]
    except:
        print("Carro não existe na lista")
    os.system("pause")

def LigarCarro():
    os.system("cls") or None
    num_car = input("Informe o número do carro que deseja ligar: ")
    
    try:
        carros[int(num_car)].ligar()
        print("Carro ligado")
    except:
        print("Carro não existe na lista")
    os.system("pause")

def DesligarCarro():
    os.system("cls") or None
    num_car = input("Informe o número do carro que deseja ligar: ")
    
    try:
        carros[int(num_car)].desligar()
        print("Carro desligado")
    except:
        print("Carro não existe na lista")
    os.system("pause")

def ListarCarros():
    os.system("cls") or None
    p = 0
    for c in carros:
        print(str(p) +" - "+ c.nome)
        p = p + 1
    os.system("pause")