# Crie uma classe chamada Musica com os seguintes atributos e crie 1 objeto.
class Musica:
    nome = ''
    artista = ''
    duracao = ''

m1 = Musica()
m1.nome = 'Oceano'
m1.artista = 'Djavan'
m1.duracao = '3:03'
print(m1.nome)

# Exercícios módulo 1 ___________ Classes _______________________________________
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]
# quando temos "__algumacoisa__" significa que é um método padrão que toda classe python vai ter
# utilize dir ou vars para visualizar objetos no print

#print(restaurante_praca)

"""
    Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
    Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
    Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
    Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
    Altere o valor do atributo nome para 'Bistrô'.
    Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
    Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
    Mude o estado da instância restaurante_pizza para ativo.
    Imprima no console o nome e a categoria da instância restaurante_praca.
"""

restaurante_praca.categoria = 'Italiana'
print(restaurante_praca.nome)

if restaurante_praca.ativo:
    print(f'O restaurante {restaurante_praca.nome} está ATIVADO.')
else:
    print(f'O restaurante {restaurante_praca.nome} está DESATIVADO.')

ativo = Restaurante.ativo
print(ativo)

restaurante_praca.nome = 'Bistrô'

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

if(restaurante_pizza.categoria == 'Fast food'): # estudar métodos para strings
    print('Verdade')
else:
    print('Mentira')

restaurante_pizza.ativo = True;

print(f'Nome: {restaurante_praca.nome} | Categoria: {restaurante_praca.categoria}')

# Exercícios módulo 2 ___________ Construtor e instanciando objetos _____________________________

class Musica:
    def __init__(obj, nome='', artista='', duracao=0):
        obj.nome = nome
        obj.artista = artista
        obj.duracao = duracao

    def __str__(obj):
        return f'{obj.nome} / {obj.artista} / {obj.duracao}'

musica1 = Musica('Shadow of Man', 'Lady Gaga', 120)
musica2 = Musica('Sorry', 'Justin Bieber', 134)

class Carro:
    def __init__(self, modelo='', cor='', ano=0, seguro=False): 
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.seguro = seguro
    
    def __str__(self):
        return f'{self.modelo}, {self.cor}, {self.ano}, {self.seguro}'

carro1 = Carro('Esportivo', 'Preto', 2000)
print(carro1)

# Exercícios módulo 3 ___________ Property e métodos de classe _____________________________

class Pessoa:
    def __init__(p, nome, idade, profissao=''):
        p.nome = nome
        p.idade = idade
        p.profissao = profissao
    
    def __str__(p):
        return f'{p.nome} | {p.idade} | {p.profissao}'

    def aniversario(p):
        p.idade += 1

    @property
    def saudacao(p):
        if p.profissao:
            return f'Olá, sou {p.nome}! Trabalho como {p.profissao}'
        else:
            return f'Olá, sou {p.nome}!'
    
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

print(pessoa1)
pessoa1.aniversario()
print(pessoa1)

"""
Desafios
    Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
    Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
    Crie uma instância da classe e imprima o valor da propriedade titular.
    Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
    Crie um método de classe para a conta ClienteBanco.
"""

class ContaBancaria:
    def __init__(c, titular, saldo, ativo='False'):
        c.titular = titular
        c.saldo = saldo
        c.ativo = ativo

    def __str__(c):
        return f'{c.titular} | {c.saldo}'
    
    @classmethod
    def ativar_conta(cls, c):
        c.ativo = True
    
conta1 = ContaBancaria('Armando Praça', 120.0)
conta2 = ContaBancaria('Chico Buarque', 1.049)

print(conta1)
print(conta2)

class ClienteBanco:
    def __init__(cb, nome, idade, endereco, cpf, profissao):
        cb.nome = nome
        cb.idade = idade
        cb.endereco = endereco
        cb.cpf = cpf
        cb.profissao = profissao

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

contaCliente = ClienteBanco.criar_conta('Ana', 1000)
print(contaCliente)
