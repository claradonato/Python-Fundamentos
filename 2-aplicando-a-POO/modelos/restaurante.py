class Restaurante:
    restaurantes = []

    def __init__(obj, nome, categoria): # obrigatoriamente quero a instância com os valores definidos
        obj._nome = nome.title()
        obj._categoria = categoria.upper()
        obj._ativo = False
        Restaurante.restaurantes.append(obj)

    def __str__(obj):
        return f'{obj._nome} | {obj._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property # pode usar pra calcular valores, etc
    def ativo(obj):
        return '✓' if obj._ativo else '✗'

    #método para os objetos
    def alternar_estado(obj):
        obj._ativo = not obj._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

# quando temos "__algumacoisa__" significa que é um método padrão que toda classe python vai ter
# utilize dir ou vars para visualizar objetos no print

restaurante_praca._nome = 'Praça 2.0'

Restaurante.listar_restaurantes()
