# Operaciones Matemáticas

# Importar bibliotecas o librerías de Funciones Matemáticas
import math

# ENTRADA DE DATOS 
# Declarar, crear o instancias variables o constantes
número_1 = float(input("Ingresa un número: ")) # CASTEO.- Conversión de un tipo de dato a otro tipo de dato
número_2 = float(input("Ingresa otro número: "))

# PROCESOS (Cálculos y operaciones matemáticas y lógicas)
suma = número_1 + número_2
resta = número_1 - número_2
multiplicación = número_1 * número_2
división = número_1 / número_2

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2) # Función(Paramétros o Argumentos)
cuadrado = número_1 ** 2
cubo = número_2 ** 3

raíz_cuadrada_1 = math.sqrt(9)
raíz_cuadrada_2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)

módulo_residuo = número_1	% número_2

# SALIDA DE DATOS
print("La suma es =", suma)
print('La resta es =', resta)
print("La multiplicación es =", multiplicación)
print("La división es =", división)
print("La potencia 1 es =", round(potencia_1, 2))
print("La potencia 2 es =", round(potencia_2, 2))
print("El módulo o residuo es =", módulo_residuo)
