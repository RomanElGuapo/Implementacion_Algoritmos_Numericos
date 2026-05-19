import sympy as sym
import numpy as np
#Activando modo ecuaciones

sym.init_session()
x = sym.symbols('x')

#Pidiendo la funcion al usuario

str_input = input('Ingresa tu funcion (euler se escribe -> E, 2x -> 2*x, x cuadrada -> x**2 )\t')

fx = sym.sympify(str_input)

#Haciendo la tabulacion
print('Para el intervalo de busqueda del metodo ingrese con numeros los siguientes parametros (solo con enteros):\n')

interval = (int(input('start\t')),int(input('stop\t'))+1)

first_iteration_flag=1
y_value=0
found_x0 = False
found_root = False

a = interval[0]
b = interval[1]

array_function = sym.lambdify(x, fx, "numpy")

print(f'\nf(x) = {fx}\n')

i=a
for j in array_function(np.array([k for k in range(a,b,1)])):
  print(f'{i}\t{j}')
  i+=1

decimals = int(input('Ingresa la cantidad de decimales de precicion que requieres para el metodo\t')) + 1

fxa = fx.evalf(decimals, subs = {x:a})
fxb = fx.evalf(decimals, subs = {x:b})

if (fxa - fxb):
  x0 = (a*fxb - b*fxa)/(fxb - fxa)
  print(f'\nDel intervalo dado, x0 es {x0}')
  found_x0 = True
else:
  print('Error de division sobre 0, prueba a ingresar un intervalo distinto')
  found_x0 = False

#Aqui termina la tabulacion y comienza el metodo como tal
if found_x0:
  fxx0 = fx.evalf(decimals, subs = {x:x0})

  if fxa * fxx0 < 0:
    k = a
  else:
    k = b

  convergence, i = 0,0

  fxk = fx.evalf(decimals, subs = {x:k})

  last_x = (x0*fxk - k*fxx0) / (fxk - fxx0)

  while(convergence < 3):

    print(f'x{i} = {last_x}')

    fxlast_x = fx.evalf(decimals, subs = {x:last_x})

    next_x = round((last_x*fxk - k*fxlast_x) / (fxk - fxlast_x), decimals)

    if (round(last_x,decimals) == round(next_x,decimals)):
      convergence+=1

    last_x =  next_x

    i+=1

    if i > 1000:
      break