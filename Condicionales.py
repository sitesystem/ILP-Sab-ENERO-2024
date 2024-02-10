# Condicionales. Mayor o menor de edad
# ENTRADA DE DATOS
# Declarar una variable
edad = int(input("Ingresa tu edad: "))

# PROCESO
if (edad >= 18 and edad <= 120):              # Rango entre (18 hasta 120)
  print("Mayor de edad")
elif (edad >= 0 and edad < 18):               # Rando entre (0 hasta menor que 18)
  print("Menor de edad")
elif (edad < 0 or edad > 120):                                         # Edad sea menor que 0 o mayor a 120
  print("Error")


# iDIOMA O lENGUAJE tiene un código binario (0000 y 11111)