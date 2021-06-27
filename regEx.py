# RegEx en Python (Regular Expressions)
# Pruebas con el módulo nativo 're'

# Un RegEx (o Expresión Regular) es una sequencia de carácteres que forman
# un patrón de búsqueda.
# RegEx puede ser usado para verificar si un string contiene un específico
# patrón de búsqueda

# Fuente: https://www.w3schools.com/python/python_regex.asp

import re

# Metacharacters -> Metacarácteres: son carácteres con significado especial

'''
[] -> Un conjunto (set) de carácteres. i.e.: "[a-m]" (de la 'a' a la 'm')
\ -> Señala una sequencia especial (también para escapar de carácteres especiales). i.e.: "\r" (fin de línea)
. -> Cualquier carácter (excepto el carácter newline). i.e.: "ho.a"
^ -> Empieza con... i.e.: "^hola" (el string empieza con 'hola')
$ -> Termina con... i.e.: "chau$" (el string termina con 'chau')
* -> Cero o más apariciones. i.e.: "aire*" ('aire' debe aparecer 0 o más veces en el string)
+ -> Una o más apariciones. i.e.: "aire+" ('aire' debe aparecer 1 o más veces en el string)
{} -> Exactamente el número de apariciones. i.e.: "al{2}" ('al' debe aparecer 2 veces en el string)
| -> Cualquiera o... i.e.: "cae|para" (Aparece 'cae' o 'para' o ambas)
() -> Capturar y agrupar
'''

# Special Sequences -> Sequencias Especiales: es un \ seguido de 
#                       uno de los caracteres de la siguiente lista y 
#                       tiene un significado especial.
'''
\A -> Devuelve una coincidencia (match) si los caracteres especificados están al principio de la cadena. i.e.: "\AÉl"

'''

# Búsqueda en un string si empieza por 'La' y termina con 'fuerte'
txt = 'La lluvia en Llavallol es fuerte.'
x = re.search('^La.*fuerte$', txt)
print(x)