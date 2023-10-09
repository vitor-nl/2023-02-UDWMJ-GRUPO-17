class Client:
    def __init__ (self, nome , sobrenome ,celular, endereço , gênero , email ):
        self.nome = nome
        self.sobrenome = sobrenome
        self.celular = celular
        self.endereço = endereço
        self.gênero = gênero
        self.email = email

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_sobrenome(self):
        return self.sobrenome

    def set_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def get_endereço(self):
        return self.endereço

    def set_endereço(self, endereço):
        self.endereço = endereço

    def get_celular(self):
        return self.celular

    def set_celular(self, celular):
        self.celular = celular

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_gênero(self):
        return self.gênero

    def set_gênero(self, gênero):
        self.gênero = gênero

 

      