class Pessoa():

    # Constructor
    def __init__(self, nome, olhos, idade, peso, altura):
        self.nome = nome
        self.olhos = olhos
        self.idade =idade
        self.peso = peso
        self.altura = altura

    def name_person(self):
        print("Nome: ", self.nome)

    def age_person(self):
        print("Idade: ", self.idade)

pessoa = Pessoa("Mauricio", "Verdes", 18, 55, 1.70)
print("Dados da pessoa")
pessoa.name_person()
pessoa.age_person()