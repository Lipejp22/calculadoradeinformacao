import math

def calcular_informacao(probabilidade):
    if probabilidade <= 0 or probabilidade >= 1:
        print('A probabilidade deve ser um valor entre 0 e 1')
        return None
    informacao = -math.log(probabilidade, 2)
    return informacao

while True:
    probabilidade = float(input("Digite a probabilidade do caractere: "))
    informacao = calcular_informacao(probabilidade)
    if informacao is not None:
        break

print("A informação do caractere é:", informacao)