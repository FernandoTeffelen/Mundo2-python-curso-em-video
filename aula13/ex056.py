somaidade = 0
médiaidade = 0
maioridadenome = 0
nomevelho = ''
totmuler20 = 0
for p in range(1, 5):
    print('----- {}º PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadenome = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadenome:
        maioridadenome = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmuler20 += 1
médiaidade = somaidade / 4
print('A média idade do grupo é de {}'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadenome, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmuler20))
