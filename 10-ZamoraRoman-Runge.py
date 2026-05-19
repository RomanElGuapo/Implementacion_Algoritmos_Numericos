import sympy as sym

#Activando modo ecuacione
sym.init_session()
x,y = sym.symbols('x y')

#Pidiendo la funcion al usuario
fxy = sym.sympify(input('Ingresa tu ecuacion (euler se escribe -> E, 2x -> 2*x, x cuadrada -> x**2 )\t'))

print('Empezando con la y evalueda, para construir la expresion y(a)= n')

y0_a = float(input('Ingrese su valor de a\t'))
y0_n = float(input('Ingrese su valor de n\t'))

h = float(input('ingrese el ancho de las bandas (h) para resolver la ecuacion diferencial\t'))

x_unknown = float(input('Ingresa el valor de x para el que quieres la solucion\t'))

yn = y0_n
print('\n')
for i in range(int((x_unknown-y0_a)/h)+1):

  xn = h*i + y0_a

  k1 = h * fxy.subs([(x,xn),(y,yn)])
  print(f'k1 = {k1} {xn} {yn} {h}')
  k2 = h * fxy.subs([(x,xn + h/2),(y,yn + k1/2)])
  print(f'k2 = {k2}')
  k3 = h * fxy.subs([(x,xn + h/2),(y,yn + k2/2)])
  print(f'k3 = {k3}')
  k4 = h * fxy.subs([(x,xn + h),(y,yn + k3)])
  print(f'k4 = {k4}\n')

  yn = yn + (1/6*(k1 + 2*k2 + 2*k3 + k4))

  print(f'y{i+1} = {yn}\n')