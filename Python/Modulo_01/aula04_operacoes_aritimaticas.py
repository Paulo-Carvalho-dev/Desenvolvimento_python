# Operadores aritméticos

# + Adição
# - subtração
# * multiplicação
# / Divisão
# ** potencia
# // divisão inteiro
# % resto da divisão

conta_1 = 5 + 2
conta_2 = 5 / 2
conta_3 = 5 ** 2
conta_4_divsao_inteira = 5 // 2
conta_5_resto = 5 % 2
#print(conta_2)

# Ordem de precedencia dos operadores

# 1. ()
# 2. **
# 3. * / // %
# 4. + -

# Exemplos

calculo_1 = 5 + (3 * 2)
calculo_2 = (3 * 5) + (4 ** 2) # 4 * 4
calculo_3 = 3 * (5 + 4) ** 2 # 9 * 9

print(calculo_1)
print(calculo_2)
print(calculo_3)

# pratica

pratica_1 = 5 + 3 * 2
pratica_2 = 5**2
pratica_3 = 19//2
pratica_4 = 19/2
pratica_5 = 18%2
pratica_6 = 81**(1/2)
pratica_7 = 4**3
pratica_8 = pow(4,3)
pratica_9 = 25**(1/2)
pratica_10 = 'oi' * 20
pratica_11 = '=-' * 20

# nome  = input('Qual é seu nome: ')
# print(f'Prazer em te conhecer {nome:>20}.') # direita
# print(f'Prazer em te conhecer {nome:<20}.') # esquerda
# print(f'Prazer em te conhecer {nome:^20}.') # centro
# print(f'Prazer em te conhecer {nome:=^20}.') # entre a palavra

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_in = n1 // n2
exp = n1 ** n2

print(f'A soma {soma} o produto é {multiplicacao} e a divisão {divisao:.2f}')
print(f'Divisão inteira {divisao_in} e a potência {exp}')
