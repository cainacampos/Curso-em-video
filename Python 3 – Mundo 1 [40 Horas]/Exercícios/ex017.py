'''import math'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto oposto: '))
'''hi = (((co ** 2)+(ca ** 2))** (1/2))
print('A hipotenusa vai medir {:.2f}'.format(hi))'''
'''hi = math.hypot(co,ca)'''
hi = hypot(co,ca)
'''hi = (((co ** 2)+(ca ** 2))** (1/2))'''
print('A hipotenusa vai medir {:.2f}'.format(hi))