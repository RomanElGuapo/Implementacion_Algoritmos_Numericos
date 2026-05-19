import sympy as sym
import numpy as np
#Activando modo ecuaciones
sym.init_session()
x = sym.symbols('x')

#Pidiendo la funcion al usuario

str_input = input('Ingresa tu funcion (euler se escribe -> E, 2x -> 2*x, x cuadrada -> x**2 )\t')

fx = sym.sympify(str_input)

#Pidiendo intervalo de integracion
print('Para el intervalo de integracion del metodo ingrese con numeros los siguientes parametros (solo con enteros):\n')

interval = (int(input('start\t')),int(input('stop\t')))

a = interval[0]
b = interval[1]

n = int(input('Ingrese el numero de bandas para calcular la integral (multiplos de 2)\t'))

h = (b - a)/n

y_values = 0

print('\n')
for i in range(n+1):
  print(f'y{i-1} = {y_values}')
  if i == 0:
    y_values += fx.subs(x,a)
  elif i == n:
    y_values += fx.subs(x,b)
  elif i%2 != 0:
    y_values += 4*fx.subs(x,a+(i*h)
    )
  elif i%2 == 0:
    y_values += 2*fx.subs(x,a+(i*h))

Area = (h/3) * y_values

print(f'\nEl area es {Area}')