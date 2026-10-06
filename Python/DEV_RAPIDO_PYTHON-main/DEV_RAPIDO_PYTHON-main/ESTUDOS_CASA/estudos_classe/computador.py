

# Marca ,Memoria ram, Placa de video
class Computador:
    def __init__(self,marca,memoria,placa_video):
        self.marca=marca
        self.memoria=memoria
        self.placa_video=placa_video

    def Ligar(self):
        print('Estou ligando')

    def Desligar(self):
        print('Estou desligando')

    def exibir(self):
        print(self.marca,self.memoria,self.placa_video)

computador1=Computador("Asus","8","Nvidia")
computador1.Ligar()
computador1.Desligar()
computador1.exibir()



