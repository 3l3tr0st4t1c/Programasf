from time import sleep

class Bichinho:
    def __init__(self:object,nome:str,fome:int,energia:int):
        self.nome=nome
        self.fome=fome
        self.energia=energia

    def alimentar(self,quantidade):
        print("Alimentando Bichinho..........")
        sleep(3)
        self.fome-=quantidade
        if self.fome < 0:
            self.fome=0
        print(f"Fome Pos alimentacao:{self.fome}")

    def brincar(self,tempo):
        if self.energia < 20:
            print("Energia baixa o bichinho nao quer brincar")
        else:
            rodada=0
            while rodada<tempo:
                print("Bichinho Brincando..........")
                self.energia-=1
                self.fome+=1
                sleep(3)
                print(f"Energia na rodada:{self.energia} fome na rodada:{self.fome}")
                rodada+=1
                

    def dormir(self):
        print("Bichinho dormindo........")
        sleep(10)
        self.energia=100
        self.fome+=20
        print("Bichinho acordou....")
        sleep(2)
        print(f"Energia atual:{self.energia} fome atual:{self.fome}")

    def __str__(self):
        return(f"caracteristicas do bichinho sao: {self.nome},{self.energia},{self.fome}")
    



if __name__ =="__main__":
    bichinho=Bichinho("Kaua",50,100)
    bichinho.alimentar(10)
    

    




            

                






         
    