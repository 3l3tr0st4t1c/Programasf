class Aluno:
    def __init__(self: object,nome:str,idade:int,n1:float,n2:float,n3:float,n4:float )->None:
        self.nome=nome
        self.idade=idade
        self.n1=n1
        self.n2=n2
        self.n3=n3
        self.n4=n4

        self.notas = [self.nome, self.idade, self.n1, self.n2, self.n3, self.n4]
        

    def calcular(self) -> None:
       
        soma = self.n1 + self.n2 + self.n3 + self.n4
        resultado = soma / 4
        print(f"A média de {self.nome} é: {resultado:.2f}")
        print(lista)
        




if __name__ =="__main__":
    aluno1=Aluno("Kauã",20,8,7,9,8)
    aluno2=Aluno("pedro",15,6,7,3,8)
    aluno3=Aluno("guilherme",44,8,7,9,8)
    
    
    lista=[aluno1,aluno2,aluno3]
    for aluno in lista:
        aluno.calcular()

