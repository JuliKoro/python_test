# Prueba del formateo f-string
# Fuente: https://realpython.com/python-f-strings/

# Sintáxis
nombre = "Julián"
edad = 20
print(f"Hola, {nombre}. Tenés {edad} años.") 
print(F"Hola, {nombre}. Tenés {edad} años.") # Puede ser F mayúscula también

# Expresiones arbitrárias
print(f"{2 * 37}") # Puedo imrpimir expresiones y operaciones directamente

def to_lowercase(input):
    return input.lower()

nom_completo = 'Julián Koroluk'
print(f"{to_lowercase(nom_completo)} es divertido.") # También puedo llamar funciones mientras imprimo

print(f"{nom_completo.lower()} es gracioso.") # O llamar métodos directos.

class Comedian: # f-string en clases
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

new_comedian = Comedian("Eric", "Idle", "74")
print(f"{new_comedian}")

