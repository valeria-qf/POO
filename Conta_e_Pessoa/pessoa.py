class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.altura = altura
    
    def envelhecer(self):
        if self.idade < 21:
            self.crescer(0.05)

        self.idade += 1

    def engordar (self, kg):
        self.peso += kg
    
    def emagrecer (self, kg):
        self.peso -= kg

    def crescer(self, tamanho):
        self.altura += tamanho

pessoa = Pessoa('valeria', 18, 65, 1.70)

print(pessoa.nome)
print(pessoa.idade)
print(pessoa.altura)
print(pessoa.peso)

pessoa.envelhecer()
print(pessoa.idade)
print(pessoa.altura)
