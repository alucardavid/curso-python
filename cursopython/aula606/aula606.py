"""
Split, Join, Enumerate em Python
"""

string = "O Brasil é o pais do futebol, o Brail é penta"

#  Divide a string por algum char especifico ou qualque string
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_1:
    print(lista_1.count(valor))

#  Juntar elementos de uma lista    
string2 = ','.join(lista_1)

print(string2)

#  Enumerate 
for indice, valor in enumerate(lista_1):
    print(f'Indice:{indice} e valor: {valor}')

    
