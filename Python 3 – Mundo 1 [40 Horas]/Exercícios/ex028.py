from random import randint
from time import sleep
computador = randint(0, 5)
jogador = int(input('Em que número entre 0 e 5 eu pensei? '))
print('processsando')
sleep(3)
if jogador == computador:
    print('você ganhou')
else:
    print('computador ganhou')
