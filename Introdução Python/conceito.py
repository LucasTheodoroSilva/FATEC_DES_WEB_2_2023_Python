nome = "Olá mundo!"
print(nome)

type(nome)

lista = []

lista.append('Notebook')
lista.append('Mouse')
lista.append('Teclado')
lista.append(12)


print(lista)

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

for elemento in lista:
    print(elemento)

nome = 'Fatec Araras'
for letra in nome:
    print(letra)

print(lista[0:2])

print(nome[0:5]) 

lista.insert(1, 'Mousepad')

print(lista)

idLista = id(lista)
print(idLista)

registro1 = ('Lucas', 'Fatec Araras')
registro2 = ('Theodoro', 'Fatec Araras')
registro3 = ('Silva', 'Fatec Araras')

lista_alunos = [registro1, registro2, registro3]

print(lista_alunos)

for elemento in lista:
    if isinstance(elemento, str):
        print(elemento)

conjunto1 = set(list(range(1,10)))
conjunto2 = set(list(range(5,16)))

print(conjunto1)
print(conjunto2)

pr1 = conjunto1.intersection(conjunto1)
pr2 = conjunto2.intersection(conjunto2)
pr3 = conjunto1.union(conjunto2)

print(pr1)
print(pr2)
print(pr3)