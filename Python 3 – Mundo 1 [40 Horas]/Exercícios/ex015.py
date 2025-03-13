
print('='*50)
print('\n'*1)

d = float(input("Quantos dias o carro ficou alugado?: "))
km = float(input("Quantos KM você rodou?: "))
valor = float((d*60) + (km*0.15))
print ('O preço ficou R$ {:.2f}'.format(valor))

print('\n'*1)
print('='*50)
