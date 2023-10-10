from client import Client

import pandas as pd
from unidecode import unidecode
import csv


print("##################################################################")
print("#                                                                #")
print("#              Seja bem-vindo à Livraria do Grupo 17             #")
print("#                                                                #")
print("##################################################################")
print("##########################      ,   ,   ##########################")
print("##########################     /////|   ##########################")
print("##########################    ///// |   ##########################")
print("##########################   |~~~|  |   ##########################")
print("##########################   |===|  |   ##########################")
print("##########################   |   |  |   ##########################")
print("##########################   |   |  |   ##########################")
print("##########################   |   | /    ##########################")
print("##########################   |===|/     ##########################")
print("##########################   '---'      ##########################")
print("##################################################################")

def dados_cliente_pedido():

    nome = input("Digite o nome do cliente: ")
    sobrenome = input("Digite o sobrenome do cliente: ")
    celular = input("Digite o número de celular do cliente: ")
    endereço = input("Digite o endereço do cliente: ")
    gênero = input("Digite o gênero do cliente: ")
    email = input("Digite o e-mail do cliente: ")

    client_dd = Client(nome=nome, sobrenome=sobrenome, celular=celular, endereço=endereço, gênero=gênero, email=email)

    return client_dd


class Livraria:
    def __init__(self, nome_arquivo_csv):
        self.nome_arquivo_csv = nome_arquivo_csv
        self.df_livros = self.ler_arquivo_csv()

    def ler_arquivo_csv(self):
        try:
            df = pd.read_csv(self.nome_arquivo_csv)
            return df
        except FileNotFoundError:
            print(f"O arquivo {self.nome_arquivo_csv} não foi encontrado.")
            return None

    @staticmethod
    def salvar_venda_csv(cliente, livro, quantidade, valor_total):
        with open('vendas.csv', mode='a', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            
            if arquivo_csv.tell() == 0:
                writer.writerow(['Nome', 'Sobrenome', 'Celular', 'Endereço', 'Gênero', 'Email', 'Título', 'Quantidade', 'Valor Total'])
            
            writer.writerow([cliente.get_nome(), cliente.get_sobrenome(), cliente.get_celular(), cliente.get_endereço(),
                            cliente.get_gênero(), cliente.get_email(), livro, quantidade, valor_total])

    def realizar_venda(self, client_dd):
        if self.df_livros is None:
            return

        print("Livros disponíveis:")
        print(self.df_livros[['Título', 'Preço Unitário', 'Quantidade']])

        titulo = input("Digite o título do livro que deseja vender: ")
        titulo = unidecode(titulo.title())

        if titulo not in self.df_livros['Título'].values:
            print(f"O livro '{titulo}' não foi encontrado na lista de livros disponíveis.")
            return

        quantidade_venda = int(input("Digite a quantidade a ser vendida: "))

        if quantidade_venda <= 0:
            print("A quantidade de venda deve ser maior que zero.")
            return

        livro = self.df_livros[self.df_livros['Título'] == titulo].iloc[0]

        if quantidade_venda > livro['Quantidade']:
            print(f"Não há estoque suficiente para vender {quantidade_venda} unidades do livro '{titulo}'.")
            return

        valor_total = quantidade_venda * livro['Preço Unitário']

        self.df_livros.loc[self.df_livros['Título'] == titulo, 'Quantidade'] -= quantidade_venda

        Livraria.salvar_venda_csv(client_dd, titulo, quantidade_venda, valor_total)
        
        print(f'Venda realizada com sucesso!\n'
              f'Título do livro: {titulo}\n'
              f'Quantidade vendida: {quantidade_venda}\n'
              f'Valor total da venda: R$ {valor_total:.2f}')
              
        print(f'Dados do cliente:    \n'
              f'Nome: {client_dd.get_nome()} \n'
              f'Sobrenome: {client_dd.get_sobrenome()} \n'
              f'Celular: {client_dd.get_celular()} \n'
              f'Endereço: {client_dd.get_endereço()} \n'
              f'Gênero: {client_dd.get_gênero()} \n'
              f'Email: {client_dd.get_email()} \n')


nome_arquivo_csv = 'livros.csv'

livraria = Livraria(nome_arquivo_csv)

if livraria.df_livros is not None:
    client_dd = dados_cliente_pedido()
    livraria.realizar_venda(client_dd)
