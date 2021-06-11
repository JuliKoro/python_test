# Built-in Functions

# Funciones nativas de Python

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