a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
# verificar o menor
menor = a
if  b<a and b<c:
    menor =b
if c<a and c<b:
    menor = c

# verificar o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('o maior valor foi {} e o menor foi {}'.format(maior, menor))