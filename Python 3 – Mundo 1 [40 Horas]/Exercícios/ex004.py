# Faça um programa que leia algo 
# pelo teclado e mostre na tela 
# o seu tipo primitivo e todas as 
# informações possoveis
print ('------------------------------------')
a = (input ('Digite um algo: '))
print ('O tipo primitivo desse valor é ', type(a))
print ('Só tem espaço? ', a.isspace())
print ('é um número? ', a.isnumeric())
print ('é afabetico? ', a.isalpha())
print ('é afanumerico? ', a.isalnum())
print ('esta em maiúsculas', a.isupper() )
print ('esta em minúscula', a.islower() )
print ('esta capitalizada', a.istitle() )
print ('------------------------------------')