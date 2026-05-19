import sympy as sym
#Activando modo ecuaciones

sym.init_session(use_unicode=True)
x = sym.symbols('x')

#Pidiendo la funcion al usuario

str_input = input('Ingresa tu funcion (euler se escribe -> E, 2x -> 2*x, x cuadrada -> x**2 )\t')

user_function = sym.sympify(str_input)

#Haciendo la tabulacion
print('Para el intervalo de busqueda del metodo ingrese con numeros los siguientes parametros (solo con enteros):\n')

first_iteration_flag=1
y_value=0
found_x0 = False
found_root = False

ran = range(int(input('start\t')),int(input('stop\t'))+1, int(input('step\t')))

for x_value in ran:
  #Columnas de inicio de la tabla
  if (first_iteration_flag):
    print(f'\nf(x) = {str_input}\n\n x \t y')
    first_iteration_flag = 0

  #solo despues del primer valor buscaremos un cambio de signo

  elif (y_value * user_function.subs(x,x_value) < 0):
    x0 = (x_value + (x_value - ran.step)) / 2
    found_x0 = True

  elif (y_value == 0):
    print(f'Se encontro la raiz en el valor {y_value}')
    found_x0 = False
    found_root = True
    break

  y_value = user_function.subs(x,x_value)
  print(f'{x_value}\t{y_value}')

if(found_x0):
  print(f'\nDel intervalo dado, x0 es {x0}')
elif (not found_root):
  print('\nNo se encontro un cambio de signo en el intervalo de la funcion')

#Aqui termina la tabulacion y comienza el metodo como tal

if (found_x0):

  gx = sym.sympify(input('Ingresa tu despeje a usar como g(x)'))
  decimals = int(input('Ingresa la cantidad de decimales de precicion que requieres para el metodo\t')) + 1
  convergence, i= 0,0
  last_x =  gx.evalf(decimals, subs = {x:x0})

  while(convergence < 3):

    print(f'x{i} = {last_x}')

    next_x =  gx.evalf(decimals, subs = {x:last_x})

    if ((round(last_x,decimals) == round(next_x,decimals))):

      convergence+=1

    last_x = next_x

    i+=1