#Implemente um script em python de modo que o usuário informe um número e o programa imprima
# como resultado todos os divisores daquele número. Este exercício deve ser implementado
# utilizando o comando for.
# Autor: Diego Vale do Nascimento - 12/10/2022
#Divisores de 60: (1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60).

n = int(input('Digite um número inteiro: '))
print('Os divisores de', (n), 'são: ')
for i in range(1, n + 1):
    if n % i == 0:
        print('{} '.format(i), end='')

