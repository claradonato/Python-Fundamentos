from .avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(obj, nome, categoria): # obrigatoriamente quero a instância com os valores definidos
        obj._nome = nome.title()
        obj._categoria = categoria.upper()
        obj._ativo = False
        obj._avaliacao = []
        obj._cardapio = []
        Restaurante.restaurantes.append(obj)

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

    def adicionar_cardapio(obj, item):
        if isinstance(item, ItemCardapio):
            obj._cardapio.append(item)

    def listar_cardapio(obj):
        for i,item in enumerate(obj._cardapio, start=1):
            if hasattr(item, 'descricao'):
                print(f'{i}. Nome: {item._nome} | Preço: {item._preco} | Descrição: {item.descricao}')
            elif hasattr(item, 'tamanho'):
                print(f'{i}. Nome: {item._nome} | Preço: {item._preco} | Tamanho: {item.tamanho}')
            else:
                print(f'{i}. Nome: {item._nome} | Preço: {item._preco} | Tamanho: {item.tam} | Tipo: {item.tipo} | Descrição: {item.desc}')

# quando temos "__algumacoisa__" significa que é um método padrão que toda classe python vai ter
# utilize dir ou vars para visualizar objetos no print
