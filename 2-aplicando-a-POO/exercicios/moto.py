from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ligado, tipo):
        super().__init__(marca, modelo, ligado)
        self.tipo = tipo
    
    def __str__(self):
        return f'Marca: {self.marca} | Tipo: {self.tipo} | Status: {self._ligado}'
    
    def ligar(self):
        print(f'A moto {self.modelo} está ligada. Vrumm vrumm 🏍️💨')