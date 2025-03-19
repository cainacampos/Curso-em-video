sal = float(input('Qual é salário do funcionário? R$'))
if sal <= 1250:
    nsal = sal * 1.15
else:
    nsal = sal * 1.10
print('Salário antigo: R${:.2f}\nSalário novo: R${:.2f}'.format(sal,nsal))