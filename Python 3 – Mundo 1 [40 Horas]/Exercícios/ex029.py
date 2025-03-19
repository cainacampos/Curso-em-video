velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO')
    multa = float(velocidade - 80) *7
    print('você foi multado em R${:.2f}'.format(multa))
else:
    print('siga com segurança')