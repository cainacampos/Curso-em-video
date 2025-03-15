num = int(input('Informa um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {:<5}'.format(u))
print('Dezena: {:<5}'.format(d))
print('centena: {:<5}'.format(c))
print('Milhar: {:<5}'.format(m))