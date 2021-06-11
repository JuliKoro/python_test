# Built-in Functions
# Funciones nativas de Python

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# -> Imrime en pantalla/archivo un objeto, que puede separarse según 'sep' y una
#    terminación según 'end'. En file, debe ir el puntero/variable de archivo a escribir.
#    Todos los argumentos que no sean palabras claves (non-keyboard) son convertidos a str().
#    'sep' y 'end' deben ser argumentos tipo string, o directamente no usarse (None)
#    Si no se pasan objetos, solo imprime 'end'.

print('¡Hola Mundo!') # Imprime un string
entero = 128
print('Numero entero: ', entero) # Imprime un string seguido de otro objeto int
print('Números: ', 1, 2, 3, 4, 5, sep=';', end='\n\n') # Imprime un string, varios obejtos
                                                    # separados por ';' y al final un salto de línea.

# abs(x) -> devuelve el valor absoluto de un número (Módulo / Norma / Valor positivo)
num_float = -5.25
modulo = abs(num_float)
print(f'Valor absoluto de {num_float}: {modulo}\n')

# all(iterable) -> Retorna True si todos los elementos de una lista son verdaderos o si está vacia
#                  Si tiene algún elemento falso retorna False.
lista_bool1 = [True, True, True]
lista_vacia = []
lista_bool2 = [True, False, True]
if all(lista_bool1) == True:
    print(f'La lista {lista_bool1} tiene elementos verdaderos.')
else:
    print(f'La lista {lista_bool1} tiene elementos falsos.')
if all(lista_vacia) == True:
    print(f'La lista {lista_vacia} tiene elementos verdaderos.')
else:
    print(f'La lista {lista_vacia} tiene elementos falsos.')
if all(lista_bool2) == True:
    print(f'La lista {lista_bool2} tiene elementos verdaderos.\n')
else:
    print(f'La lista {lista_bool2} tiene elementos falsos.\n')

# any(iterable) -> Retorna True si hay algún elemento verdadero en la lista
#                  Retorna False si la lista está vacia.
if any(lista_bool2) == True:
    print(f'La lista {lista_bool2} tiene elemento/s.')
else:
    print(f'La lista {lista_bool2} está vacia.')
if any(lista_vacia) == True:
    print(f'La lista {lista_vacia} tiene elemento/s.\n')
else:
    print(f'La lista {lista_vacia} está vacia.\n')

# repr(object) -> 

# ascii(object) ->

# format(value, format_spec) -> Convierte un valor (x) en un formato específico (format_spec)
# Existe una sintaxis de formateos estándar:
# https://docs.python.org/3.7/library/string.html#formatspec
# El formateo dpor defecto de format_spec es un string vacio que resulta el mismo efecto
# de llamar a str(value)
hexa = format(entero, 'x') # Convierte un entero a base hexadecimal
print(f'El nro. {entero} en hexadecimal es: {hexa}\n')

# bin(x) -> Convierte a un entero en binario, prefijado con "0b"
binario = bin(entero)
print(f'{entero} en bineario es: {binario}')
# Otra opción para convertir y sacandole el prefijo "0b":
binario = format(entero, 'b')
print(f'Binario sin prefijo: {binario}')
# ó directamente imprimiendo:
print(f'Binario sin prefijo 2: {entero:b}')

# class bool([x]) -> 