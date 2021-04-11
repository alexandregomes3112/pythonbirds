class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=44):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Hola mi nombre és {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 45

    @classmethod
    def nome_att_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_classe = super().cumprimentar()
        return f'{cumprimentar_classe}. Dá-me Tu Mano Cabrón !'


class Mutante(Pessoa):
    olhos = 4


if __name__ == '__main__':
    alexandre = Homem(nome='Alexandre')
    pituca = Pessoa(alexandre, nome='Pituca')
    pituca.idade = 9
    print(Pessoa.cumprimentar(pituca))
    print(id(pituca))
    print(pituca.cumprimentar())
    print(pituca.nome)
    print(pituca.idade)
    for filho in pituca.filhos:
        print(filho.nome)
    alexandre.sobrenome = "Gomes"
    print(alexandre.sobrenome)
    print(alexandre.__dict__)
    print(pituca.__dict__)
    # del alexandre.olhos
    print(Pessoa.olhos)
    print(alexandre.olhos)
    print(pituca.olhos)
    print (id(Pessoa.olhos), id(alexandre.olhos), id(pituca.olhos))
    print(Pessoa.metodo_estatico(), alexandre.metodo_estatico())
    print(Pessoa.nome_att_classe(), alexandre.nome_att_classe())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(alexandre, Pessoa))
    print(isinstance(alexandre, Homem))
    print(alexandre.olhos)
    print(alexandre.cumprimentar())
    print(pituca.cumprimentar())
