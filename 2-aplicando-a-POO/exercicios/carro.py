from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ligado, qtd_portas, cor):
        super().__init__(marca, modelo, ligado)
        self.qtd_portas = qtd_portas
        self.cor = cor

    def __str__(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Quantidade Portas: {self.qtd_portas} | Cor: {self.cor}'
    
    def ligar(self):
        print(f'O carro {self.modelo} está ligado. Vrumm vrumm 🚗💨')