class Pessoa:
    def __init__(self, nome=None, idade=44):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Pituca')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Élékizander'
    print(p.nome)