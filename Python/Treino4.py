num = int(input("Insira um número aqui: "));

lista_rn = range(1,num+1);

lista_div = [];

for numero in lista_rn :
    if num % numero == 0 :
        lista_div.append(numero);
print(lista_div);