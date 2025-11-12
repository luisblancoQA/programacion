# Tipos de datos bàsicos - Ejemplo práctico
numero_entero = 46   # int
numero_decimal = 1.75   # float
nombre = "Luis"   # str
es_estudiante = True   # bool

# Mostrar valores y tipos
print("Número Entero:", numero_entero, type(numero_entero))
print("Número Decimal:", numero_decimal, type(numero_decimal))
print("Nombre:", nombre, type(nombre))
print("¿Es estudiante?", es_estudiante, type(es_estudiante))

# Conversión de tipos (Casting)
edad = "46"
edad_numero = int(edad)   # De texto a número

altura = 1.75
altura_texto = str(altura)

print(edad_numero + 4)   # Ahora si se puede sumar
print("Tu altura es", altura_texto)



