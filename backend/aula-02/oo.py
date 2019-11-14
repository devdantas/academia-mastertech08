class Mamiferos():
    # Default values
    olhos = 2
    patas = 4

    # Constructor
    def __init__(self, pelo, especie, rabo, cor):
        self.pelo = pelo
        self.especie = especie
        self.rabo = rabo
        self.cor = cor

    def comer(self):
        print("Comi")

    def fazer_som(self):
        print("Som")

mamifero = Mamiferos("curto", "doguinho caninus", True, "caramelo")
mamifero_two = Mamiferos("longo", "agrarios monata", False, "purple")

mamifero.comer()
mamifero_two.fazer_som()
print(mamifero.especie)
print(mamifero_two.especie)

class Gato(Mamiferos):

    # Constructor
    def __init__(self, pelo, especie, rabo, cor, bigodes):
        super().__init__(pelo, especie, rabo, cor)
        self.bigodes = bigodes

    def fazer_som(self):
        print("MIAU")

gatinho = Gato("super curto", "peladus egiptum", True, "bege organico", 5)

print("--------------------------------")
print(gatinho.especie)
print(gatinho.bigodes)
gatinho.fazer_som()