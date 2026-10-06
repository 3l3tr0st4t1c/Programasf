import pickle
import os

def binary(dados:dict)->None:
    try:
        with open("dados.bin","wb")as salva_binario:
            pickle.dump(dados,salva_binario)
        print("Dados salvos com sucesso")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os dados: {e}")


    try:
        with open("dados.bin","rb") as carrega_binario:
            dados_carregados=pickle.load(carrega_binario) 
        print("Dados carregados com sucesso:",dados_carregados)
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados:{e}") 
        
def binario2():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    dados_binario_nome = os.path.join(diretorio_atual, "dados_puros.bin")
    
    frase= "O rato roeu a ropa do kauã no valaum, se liga meci kkkkkkkkkkkkkkkk"
    dados_binarios = frase.encode('utf-8')
    
    try:
        with open(dados_binario_nome, "wb") as salva_binario:
            salva_binario.write(dados_binarios)
        print("Dados binários salvos com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados binários: {e}")
        
    if os.path.exists(dados_binario_nome):
        try:
            with open(dados_binario_nome, "rb") as carrega_binario:
                dados_carregados_bytes = carrega_binario.read()

                dados_carregados_texto = dados_carregados_bytes.decode('utf-8')
                
                binario_real = " ".join(f"{byte:08b}" for byte in dados_carregados_bytes)
                
            print("Dados carregados com sucesso: ")
            print(f"{binario_real} -> {dados_carregados_texto}")
        
        except Exception as e:
            print(f"Ocorreu um erro ao carregar os dados binários: {e}")  
        

if __name__ =="__main__":
    dados={"nome":"Kaua","idade":19,"Profissao":"Garoto de Programa"}
    binary(dados)
    binario2()