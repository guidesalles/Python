# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa:
    def __init__(self, nome , cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def cadastroCompleto(self):
        print(self.nome + " mora em " + self.cidade + " , tem o celular: " + self.telefone + " e e-mail: " + self.email)



pessoa1 = Pessoa("Guilherme", "Araruama", "981248202", "dexter342@gmail.com")

pessoa1.cadastroCompleto()

