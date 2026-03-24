# Calculadora com while

"""
sair = input('Quer sair? [s]im: ').lower().startswith('s')
nesse trecho estamos fazendo um vaerificação e tratando o que úsuario esta nos enviando

logo abaixo uma condição de parada break

"""


while True:

    # solicitando os dados para úsuario
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None # Bandeira (flag)

    # tratando erros
    try:
        numero_1_flot = float(numero_1)
        numero_2_flot = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    # condição
    if numeros_validos is None:
        print('Um ou ambos os números digitados não são validos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido.')
        continue

    if len(operador) > 1:
        print('Digite apenas 1 operador')
        continue

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break

