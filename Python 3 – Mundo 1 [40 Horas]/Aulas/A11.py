# sempre quando eu quiser representar uma cor no python eu vou usar 
# esse código: \033[m
# pode ter 3 códigos: um de style, text, back
# style: 0 (None); 1 (negrito); 4(underline); 7 (Negative, inverter fundo)
# texto: todos com número 30 até 37
# back: todos com número 40 até 47

print('\033[7;31;43mtest\033[m')
a = 7
b = 3
print('Os valores são \033[32;1m{}\033[m e \033[36;1m{}\033[m'.format(a,b))
nome = 'Cainã'
print('Olá, muito prazer em te conhecer {}{}{}!!!!'.format('\033[1;4;7;30;43m',nome,'\033[m'))