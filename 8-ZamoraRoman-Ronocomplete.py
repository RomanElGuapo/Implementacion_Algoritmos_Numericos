import sympy as sym
import numpy as np

#Empezamos implementando trapecios

def trapecios(funcion, intervalo, n):
  a = intervalo[0]
  b = intervalo[1]

  h = (b - a)/ n

  y_values = 0

  for i in range(n+1):
    if i == 0:
      y_values += funcion.evalf(5, subs = {x:a}) / 2

    elif i == n:
      y_values += funcion.evalf(5, subs = {x:b})/2

    else:
      y_values += funcion.evalf(5, subs = {x:a + i*h})

  area = h * y_values

  return area

#Activando modo ecuaciones

sym.init_session()

x = sym.symbols('x')

fx = sym.sympify(input('Ingresa tu ecuacion\t'))
interval = (float(input('Ingresa el inicio de tu intervalo\t')), float(input('Ingresa el final\t')))
k = int(input('Ingresa tu k numero de iteraciones'))

i_matrix = np.zeros((k,k))
for i in range(k):
  i_matrix[0][i] = trapecios(fx,interval, 2**i)

i_matrix