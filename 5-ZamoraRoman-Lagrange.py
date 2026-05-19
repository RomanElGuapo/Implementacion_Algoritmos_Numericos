import numpy as np
import sympy as sym

#Activando modo calculadora

sym.init_session()
x,y,z = sym.symbols('x y z')

#Obteniendo las ecuaciones del usuario

n = 3#int(input('Ingresa el numero de incognitas de tu sistema\t'))

print('Ingresa una ecuacion igualada a 0 por incognita (Solo 3 incognitas)\nEjemplo:\n8*x -y +2*z -10\nx -9*y +z +8\n3*x +y -12*z +12\n')

equations = []

for i in range(n):
  equations.append(sym.sympify(input(f'ecuacion {i+1}\t')))

x_equation = sym.Eq(equations[0],0)
x_equation = sym.solve(x_equation, x)[0]

y_equation = sym.Eq(equations[1],0)
y_equation = sym.solve(y_equation, y)[0]

z_equation = sym.Eq(equations[2],0)
z_equation = sym.solve(z_equation, z)[0]

decimals = int(input('Ingresa la cantidad de decimales de precicion que requieres para el metodo\t')) + 1

last_x = x_equation.evalf(decimals, subs = {y:0, z:0})

last_y = y_equation.evalf(decimals, subs = {x:last_x, z:0})

last_z = z_equation.evalf(decimals, subs = {x:last_x, y:last_y})


convergence, i = 0,0

while(convergence < 3):

  print(f'\nx{i} = {last_x}')
  print(f'y{i} = {last_y}')
  print(f'z{i} = {last_z}\n')

  next_x = x_equation.evalf(decimals, subs = {y:last_y, z:last_z})

  next_y = y_equation.evalf(decimals, subs = {x:last_x, z:last_z})

  next_z = z_equation.evalf(decimals, subs = {x:last_x, y:last_y})

  if (round(last_x,decimals) == round(next_x,decimals) and
      round(last_y,decimals) == round(next_y,decimals) and
      round(last_z,decimals) == round(next_z,decimals)):
    convergence+=1

  last_x =  next_x
  last_y =  next_y
  last_z =  next_z

  i+=1

  if i > 1000:
    break