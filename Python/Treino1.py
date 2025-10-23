import datetime

ano_atual = datetime.datetime.now().year;
nome = str(input("Qual o seu nome? "));
idade = int(input("Qual a sua idade? "));
print(f"{nome}, você terá 100 anos em {ano_atual - idade + 100}")