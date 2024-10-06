print('Calcule a area de um quadrado')
lado = float(input('Informe o valor do lado:'))
area_quadrado = lado**2
print(f'o resultado da area do quadrado é {area_quadrado}')

print('Calcular a area do trapezio!')
B = float(input('informe a base maior:'))
b = float(input('informe a base menor:'))
h = float(input('informe a altura:'))
area_do_trapezio =  (B + b)* h/2
print(f'resultado da area do trapezio é {area_do_trapezio}')

print("Calcule a area do triangulo!")
bb = float(input('informe o valor da base:'))
hh = float(input('informe o valor da altura:'))

area_do_triangulo = bb*hh/2
print(f'o resultado da area do triangulo é {area_do_triangulo}')

if area_quadrado > area_do_triangulo and area_quadrado > area_do_trapezio:
    print('Area do quadrado é maior!')
elif area_do_triangulo > area_quadrado and area_do_triangulo > area_do_trapezio:
    print('Area do triangulo é maior!')
elif area_do_trapezio > area_quadrado and area_do_trapezio > area_do_triangulo:
    print('Area do trapezio é maior!')
else:
    print('Todos estão erradas!')



