from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'gourmet')
bebida_suco = Bebida('Suco de melância', 4.5, 'Grande')
prato_paozin = Prato('Pão de queijo', 0.8, 'Mineiro')
restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_paozin)
bebida_suco.aplicar_desconto()
prato_paozin.aplicar_desconto()
sobremesa_pudim = Sobremesa('Pudim', 8.0, 'Tradicional', 'Médio', 'Com calda doce')
restaurante_praca.adicionar_cardapio(sobremesa_pudim)

def main():
    restaurante_praca.listar_cardapio();

if __name__ == '__main__':
    main()
