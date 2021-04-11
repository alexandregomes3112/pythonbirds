class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=44):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    alexandre = Pessoa(nome='Alexandre')
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
    alexandre.olhos = 1
    # del alexandre.olhos
    print(Pessoa.olhos)
    print(alexandre.olhos)
    print(pituca.olhos)
    print (id(Pessoa.olhos), id(alexandre.olhos), id(pituca.olhos))
