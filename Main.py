from biblioteca import Biblioteca

class Main:
    def __init__(self):
        self.biblioteca = Biblioteca()

    def executar(self):
        while True: #Menu
            print("\nEscolha uma opção:")
            print("1. Adicionar livro")
            print("2. Listar livros")
            print("3. Vender Livro")
            print("4. Sair")

            escolha = input("Opção: ")

            if escolha == '1':
                titulo = input("Título do livro: ")
                autor = input("Autor do livro: ")
                ano = input("Ano de publicação: ")
                valor = input("Valor do livro: ")
                quantidade = input("Quantidade disponível: ")
                self.biblioteca.AddLivro(titulo, autor, ano, valor, quantidade)
            elif escolha == '2':
                self.biblioteca.ListLivro()
            elif escolha == '3':
                #venda de livro coloque o codigo
            elif escolha == '4':
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    programa = Main()
    programa.executar()