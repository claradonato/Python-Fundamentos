# Exercícios

# Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
livros_kafka = ['A Metamorfose', 'O Processo']
for livro in livros_kafka:
    print(livro)

# Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma = 0
for num in range(1, 11):
    if num%2 != 0:
        soma += num
print(soma)

# Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente. 
for num in range(10, 0, -1):
    print(num)

# Solicite ao usuário um número e, em seguida, utilize um loop for para 
# imprimir a tabuada desse número, indo de 1 a 10.
num = int(input('Digite um numero: '));
for tab in range(1, 11):
    print(f'{num} x {tab} = {num*tab}')

#Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.
soma_lista = 0
numeros = [1, 4, 2, 5, 6]
try:
    for elem in numeros:
        soma_lista += elem
    print(soma_lista)
except Exception as e:
    print(f'Ocorreu um erro: {e}')


# Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
valores = [8.0, 9.0, 10, 8.7]
media = 0

try:
    for valor in valores:
        media += valor
    media = media / len(valores)
    print(f'Média dos valores: {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

# Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoa = {'nome': 'Franz Kafka', 'idade': 25, 'cidade': 'Praga'}

#Utilizando o dicionário criado no item 1:
#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa; Remova um item do dicionário.

pessoa['idade'] = 26
pessoa['profissao'] = 'Escritor'
del pessoa['cidade']

#Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

#Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário. 
filosofos = [{'nome': 'Platão', 'obra': 'Os últimos dias de Sócrates'}, {'nome': 'Dostoiévski', 'obra': 'Noites brancas'}]

if 'obra' in filosofos:
    print('A chave obra existe no dicionário')
else:
    print('A chave não existe no dicionário')

# Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase_kafka = 'Mesmo no caso de a esperança ser muito pequena, não tenho o direito de não usar as minhas possibilidades'
contar_palavras = {}
palavras = frase_kafka.split()
for palavra in palavras:
    contar_palavras[palavra] = contar_palavras.get(palavra, 0) + 1
print(contar_palavras)
