#Criação e estrutura condicional para lista
lista = ['Python', 'Science', 24, 2.4, True]
print(lista)

print(len(lista))

if(lista[4] == True):
    print('its true')
else:
    print('its false')

#Partição por indexação
lista2 = lista[1:3] 
print(lista2)

#adiciona no final da lista
print('Método append()')
lista.append('Data')
print(lista)

#adiciona vários elementos no final da lista
print('Método extend()')
lista.extend([False, 'Methods', 3])

#remove elemento específico da lista
print('Método remove()')
lista.remove(2.4)

raca_caes = ['Labrador Retriever',
             'Bulldog Francês',
             'Pastor Alemão',
             'Poodle']

#insere um elemento em uma posição específica
#sintaxe lista.insert(indice, elemento)

raca_caes.insert(1, 'Golden Retriver')

raca_caes.insert(len(raca_caes), 'Husky Siberiano')

#remove e retorna elemento de uma posição
print(raca_caes.pop(1))

#retorna o índice de um elemento da lista
print(raca_caes.index('Pastor Alemão'))

#ordenada a lista em crescente ou decrescente
raca_caes.sort()
print(raca_caes)
