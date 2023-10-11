import csv

class Biblioteca:
    def __init__(self):
        self.biblioteca = self.CarregaBiblioteca()

    #adicionar Livro
    def AddLivro(self, titulo, autor, ano, valor, quantidade):
        livro = {
            "Título": titulo,
            "Autor": autor,
            "Ano": ano,
            "Valor": valor,
            "Quantidade": quantidade
        }
        self.biblioteca[titulo] = livro
        self.SalvaBiblioteca()  
    #Listar Livro
    def ListLivro(self):
        print("Livros na biblioteca:")
        for titulo, livro in self.biblioteca.items():
            print(f"Título: {livro['Título']}, Autor: {livro['Autor']}, Ano: {livro['Ano']}, Valor: {livro['Valor']}, Quantidade: {livro['Quantidade']}")
    #salvar na biblioteca
    def SalvaBiblioteca(self):
        with open('biblioteca.csv', 'w', newline='') as arquivo_csv:
            GravCSV = csv.writer(arquivo_csv)
            GravCSV.writerow(["Título", "Autor", "Ano", "Valor", "Quantidade"])
            for livro in self.biblioteca.values():
                GravCSV.writerow(livro['Título'], livro['Autor'], livro['Ano'], livro['Valor'], livro['Quantidade'])
        print("Biblioteca salva em 'biblioteca.csv'")
    #mostar biblioteca
    def CarregaBiblioteca(self):
        biblioteca = {}
        try:
            with open('biblioteca.csv', 'r') as arquivo_csv:
                LerCSV = csv.DictReader(arquivo_csv)
                for linha in LerCSV:
                    titulo = linha["Título"]
                    autor = linha["Autor"]
                    ano = linha["Ano"]
                    valor = linha["Valor"]
                    quantidade = linha["Quantidade"]
                    biblioteca[titulo] = {
                        "Título": titulo,
                        "Autor": autor,
                        "Ano": ano,
                        "Valor": valor,
                        "Quantidade": quantidade
                    }
            return biblioteca
        except FileNotFoundError:
            return {}