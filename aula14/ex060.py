n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('Calculando fatorial de {}:  '.format(n), end='')
while c > 0:
    print('{}'.format(n, f), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
