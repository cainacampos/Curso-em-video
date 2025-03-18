n = str(input('Digite seu nome completo: ')).strip()
nome = n.split() 
'''Essa função split transforma uma frase ou nome em uma 
lista com o seu conteudo. Cainã Campos se
transforma em dois elementos ['Cainã', 'Campos']
Ele vai fatiar'''
print('Primeiro nome: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))
