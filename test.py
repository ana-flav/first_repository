class SmartTv:
    def __init__(self):
        self.volume = 10
        self.canal = 25
        self.ligar = False

    def ligarTv(self):
        self.ligar = True
        return self.ligar
       
    def escolherCanal(self, canal_x):
        self.canal = canal_x
        return self.canal
    
    def aumentarVolume(self):
        self.volume +=1
        return self.volume
    
    def abaixarVolume(self):
        self.volume -=1
        return self.volume


class Usuario:
    def __init__(self):
        self.nome = 'ana'
    
    p = SmartTv()
    print(p.aumentarVolume())
    def escolhaUser(self, value):
        if value == 1:
            print(self.p.ligarTv())
        elif value == 2:
            print(self.p.aumentarVolume())
        elif value == 3:
            print(self.p.abaixarVolume())
        else:
            ouvido = int(input("diga qual canal voce quer colocar"))
            print(self.p.escolherCanal(ouvido))
def main():
        valor = int(input("Digite o que você vc gostaria fazer\n1-ligar Tv\n2-AumentarVolume\n3-AbaixarVolume\n4-Mudar de Canal"))
        info = Usuario()
        info.escolhaUser(valor)
    
if __name__ == '__main__':
    main()



      
