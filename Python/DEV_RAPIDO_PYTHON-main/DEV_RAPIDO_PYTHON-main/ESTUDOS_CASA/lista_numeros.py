def lista_num(*numeros):
    maior=numeros[0]
    for j in numeros:
        if j > maior:
            maior=j
    print(maior)





lista_num(1,2,3,4,99)