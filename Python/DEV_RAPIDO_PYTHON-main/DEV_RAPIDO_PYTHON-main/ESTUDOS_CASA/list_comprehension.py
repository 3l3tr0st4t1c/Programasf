def vivo(lista: list):
    for jogador in lista:
        if jogador["vivo"]==True:
            print(f"{jogador} está vivo")
        else:
            print(f"{jogador} morto")
       
       

        
         
        
    


if __name__ == "__main__":
    jogadores = [
    {"nome": "FalleN", "kda": 1.5, "vivo": True},
    {"nome": "S1mple", "kda": 0.8, "vivo": False},
    {"nome": "ZywOo", "kda": 2.1, "vivo": True}
]

    vivo(jogadores)