class ContaBancaria:
    def __init__(self:object,titular:str,saldo:int,historico:list):
        self.titular=titular
        self.saldo=saldo
        self.historico=historico

    def depositar(self,valor):
        log=(f"Deposito de:{valor} na conta de:{self.titular}")
        self.saldo+=valor
        self.historico.append(log)
        print(f"Valor depositado com Sucesso saldo atual:{self.saldo}")

    def sacar(self,valor):
        if valor > self.saldo:
            print("Saldo Insuficiente!")
        else:
            self.saldo-=valor
            print(f"saque de {valor} realizado com sucesso")
            log=(f"Usuario :{self.titular}, sacou:{valor}, ficando com saldo de :{self.saldo}")
            self.historico.append(log)

    def ver_historico(self):
        for i in self.historico:
            print(i)
        print(f"Saldo atual:{self.saldo}")

if __name__=="__main__":
    dados=ContaBancaria("Kaua",0,[])
    dados.depositar(40)
   





