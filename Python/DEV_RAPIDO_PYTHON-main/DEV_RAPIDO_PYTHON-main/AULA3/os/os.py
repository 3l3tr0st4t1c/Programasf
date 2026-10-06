import os
def diretorio():
    diretorio_arquivo=os.path.dirname(os.path.abspath(__file__))

    diretorio_base = "C:\\Users\\aluno\\Downloads\\python\\aula2\\os"
    subdiretorio='aula2\\os\\os.py'
    nome='dados.txt'
    caminho_relativo=os.path.join(diretorio_base,subdiretorio,nome)
    caminho_absoluto=os.path.abspath(caminho_relativo)
    print(f"caminho relativo {caminho_relativo}")
    print(f"caminho absoluto : {caminho_absoluto}")

    print(f'''todos os caminhos feitos aqui sao apenas juncoes de strings,apenas o {diretorio_arquivo}realmente é um caminho valido nesse diretorio ''')

if __name__ == "__main__":
    diretorio()