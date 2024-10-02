print('{:=^40}'.format(' LOJA DO NANDIN '))
preço = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartáo''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será e, 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totParc = int(input('Quantas parcelas? '))
    parcela = total / totParc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(total, parcela))
    print('Sua compra será e, 2x de R${:.2f}.'.format(parcela))
else:
    total = preço
    print('OPÇÃO INVALIDA de pagamento. tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
