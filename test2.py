
import random


import utils


# value = '753BC-747BC'
# value = '1BC-1AD'
value = '2000AD-2012AD'

value = value.split('-')

a1 = utils.clearNumber(value[0])
a2 = utils.clearNumber(value[1])

r1 = utils.romanoNumero(a1)
r2 = utils.romanoNumero(a2)

salida = utils.maxLetras(r1,r2)

print('El numero de reserva es: {}'.format(salida))
