from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ligado):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Ligado: {self._ligado}'
    
    @abstractmethod
    def ligar(self):
        pass
