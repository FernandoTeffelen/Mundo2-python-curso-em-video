soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c     #mesma coisa que o de baixo!
        cont += 1           #mesma coisa que o de cima!
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
