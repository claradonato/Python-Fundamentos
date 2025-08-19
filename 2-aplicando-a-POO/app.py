from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')

def main():
    restaurante_praca.receber_avaliacao('Reperquilson', 3)
    restaurante_praca.receber_avaliacao('Paola Carosella', 5)
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()