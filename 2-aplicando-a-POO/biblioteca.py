from exercicios import Livro

livro1 = Livro('Noites brancas', 'Fiódor Dostoiévski', 1848)
livro2 = Livro('O Processo', 'Franz Kafka', 1925)

def main():
    print(livro1.disponivel)
    livro1.emprestar()
    print(livro1.disponivel)

    livro_disponivel = Livro.verificar_disponibilidade(1848)
    print(f'Livros publicados disponíveis: {livro_disponivel}')

if __name__ == '__main__':
    main()