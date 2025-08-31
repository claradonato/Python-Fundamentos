from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod # todas as classes derivadas devem ter esse desconto implementado
    def aplicar_desconto(self):
        pass