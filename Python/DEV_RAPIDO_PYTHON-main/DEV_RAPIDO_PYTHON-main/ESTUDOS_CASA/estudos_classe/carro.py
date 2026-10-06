class Carro:
    def __init__(self:object,marca:str,ano:int,km_rodados:str):
        self.marca=marca
        self.ano=ano
        self.km_rodados=km_rodados


    def exibir(self):
        print(self.marca,self.ano,self.km_rodados)

    def Andar_frente(self):
        print("Andando para frente")

    def Andar_Tras(self):
        print("Andando para tras")



carro1=Carro("Civic",2019,"1000km")
carro1.exibir()
carro1.Andar_frente()
carro1.Andar_Tras()