print('='*50)
print('\n'*1)


nome = str(input('Digite seu nome Completo: ')).strip() # Acertei
print('Analisando seu nome...') # Acertei
print('Seu nome em maiúsculas é {}'.format(nome.upper())) # Acertei
print('Seu nome em minúsculas é {}'.format(nome.lower())) # Acertei
# print('Seu nome tem ai todo {} letras'.format(len(nome))) # Errei. Não tirei o espaço
# desde o começo ele usa o dividir 
print('Seu nome tem ai todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome é {} e ele tem {} letras'.format(len(nome.split()))) #Errei
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) 
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

print('\n'*1)
print('='*50)