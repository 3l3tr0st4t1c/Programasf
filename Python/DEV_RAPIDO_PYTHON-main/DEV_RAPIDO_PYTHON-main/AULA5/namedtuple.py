from collections import namedtuple



Aluno=namedtuple("Estudante",["nome","idade","trabalho"])
a=Aluno("Kaua",20,"Milionario")

print(a[1])
print(a.nome)
print(a.idade)
print(a.trabalho)
