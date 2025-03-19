'''d = float(input('Qual a distância que você vai pecorrer na sua viagem? :'))
if d <= 200:
    v = float(d * 0.5)
    print('Você pecorreu menos de 200 km, o preço ficou em R${:.2f}'.format(v))
else:
    v = float(d * 0.45)
    print('Você ganhou um desconto, vai pagar R${:.2f}'.format(v))'''

#Fiz dessa forma, o professor já simplificou em uma maneira que só usa um print

'''d = float(input('Qual a distância que você vai pecorrer na sua viagem? :'))
if d <= 200:
    v = float(d * 0.5)
else:
    v = float(d * 0.45)
print('Você ganhou um desconto, vai pagar R${:.2f}'.format(v))'''

#Ele fez um "if" simplificado

d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(d))
p = d * 0.50 if d <= 200 else d * 0.45
print('o valor da passagem ficou em R${:.2f}'.format(p))