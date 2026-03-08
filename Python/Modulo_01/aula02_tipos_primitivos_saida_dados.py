# Tipos primitivos saida de dados

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2

# Format sintax mais antiga
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
# f-string mais nova
print(f'A soma entre {n1} e {n2} vale {soma}')
