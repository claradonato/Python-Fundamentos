from .avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    tam_max = 5

    def __init__(obj, nome, categoria): # obrigatoriamente quero a instância com os valores definidos
        obj._nome = nome.title()
        obj._categoria = categoria.upper()
        obj._ativo = False
        Restaurante.restaurantes.append(obj)
        obj._avaliacao = []

    def __str__(obj):
        return f'{obj._nome} | {obj._categoria}'
    
    @property # pode usar pra calcular valores, etc
    def ativo(obj):
        return '✓' if obj._ativo else '✗'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | '
              f'{"Categoria".ljust(25)} | '
              f'{"Avaliação".ljust(25)} | '
              f'{"Status"}')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | '
                  f'{restaurante._categoria.ljust(25)} | '
                  f'{str(restaurante.media_avaliacoes()).ljust(25)} | '
                  f'{restaurante.ativo}')

    
    #método para os objetos
    def alternar_estado(obj):
        obj._ativo = not obj._ativo

    def receber_avaliacao(obj, cliente, nota):
        if 0 < nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            obj._avaliacao.append(avaliacao)

    def media_avaliacoes(obj):
        if not obj._avaliacao:
            return '-'
        
        soma = sum(avaliacao._nota for avaliacao in obj._avaliacao)
        quant_notas = len(obj._avaliacao)
        media = round(soma/quant_notas, 1)
        return media

# quando temos "__algumacoisa__" significa que é um método padrão que toda classe python vai ter
# utilize dir ou vars para visualizar objetos no print
