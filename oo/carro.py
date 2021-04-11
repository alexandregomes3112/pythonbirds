"""
  N
O   L
  S

    Exemplo:
    >>> #Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calc_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calc_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calc_velocidade()
    2
    >>> carro.frear()
    >>> carro.calc_velocidade()
    0
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_direita()
    >>> carro.calcular_direcao()
    >>> 'Leste'
    >>> carro.girar_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Oeste'


"""

NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'

class Direcao:
    rotacao_direita_dct={
        NORTE: LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE
    }
    rotacao_esquerda_dct={
        NORTE: OESTE, OESTE:SUL, SUL:LESTE, LESTE:NORTE
    }
    def __init__(self):
        self.valor = NORTE

    def girar_direita(self):
        self.valor=self.rotacao_direita_dct[self.valor]
    def girar_esquerda(self):
        self.valor=self.rotacao_esquerda_dct[self.valor]



class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
