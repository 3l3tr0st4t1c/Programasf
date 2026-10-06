def contador(dicionario: dict):
    texto = input("Digite um texto aqui: ").strip()

    numero = 1

    for caractere in texto:
        if caractere.isspace():
            continue

        dicionario[numero] = caractere
        numero += 1

    print(dicionario)


if __name__ == "__main__":
    dicionario = {}

    contador(dicionario)