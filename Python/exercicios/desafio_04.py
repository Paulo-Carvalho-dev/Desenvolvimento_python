# Faça um programa que leia algo
# pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ele

variavel = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(variavel)}')
print(f'Só tem espaços {variavel.isspace()}')
print(f'É um número? {variavel.isnumeric()}')
print(f'É alfabetico? {variavel.isalpha()}')
print(f'É alfanumerico? {variavel.isalnum()}')
print(f'Está em maiuscula? {variavel.isupper()}')
print(f'Está em minuscula? {variavel.islower()}')
print(f'Está capitalizado? {variavel.istitle()}')
