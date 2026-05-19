import sympy as sym

#Activando modo ecuacione
sym.init_session()
x,y = sym.symbols('x y')

#Pidiendo la funcion al usuario
print('Empezando con la y evalueda, para construir la expresion y(a)= n')

y0_a = float(input('Ingrese su valor de a\t'))
y0_n = float(input('Ingrese su valor de n\t'))

fxy = sym.sympify(input('Ingresa tu ecuacion (euler se escribe -> E, 2x -> 2*x, x cuadrada -> x**2 )\t'))

h = float(input('ingrese el ancho de las bandas (h) para resolver la ecuacion diferencial\t'))

x_unknown = float(input('Ingresa el valor de x para el que quieres la solucion\t'))

for i in range(int((x_unknown-y0_a)/h)+1):
  print(f'y{i} = {y0_n}')
  y0_n = y0_n + h*fxy.subs([(x,h*i),(y,y0_n)])