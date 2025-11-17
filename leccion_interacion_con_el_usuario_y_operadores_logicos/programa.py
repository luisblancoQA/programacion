# Pedimos los datos al usuario
edad = int(input("¿Cuántos años tenés?"))   # Usa int() porque todo lo que escribe el usuario llega como texto (str) incluso números
tiene_licencia = input("Tenés licencia de conducir? (sí/no) : ")

# Convertimos la respuesta en un valor booleano
if tiene_licencia.lower() == "sí" or tiene_licencia.lower() == "si":   # lower() convierte todas las letras de un texto a minúsculas. Sirve para que no importe si el usuario escribe "Sí", "sí", "SI", Si, etc.
    tiene_licencia = True
else:
    tiene_licencia = False

# Verificamos si puede conducir
if edad >= 18 and tiene_licencia:
    print("✅ Podés conducir.")
else:
    print("❌ No podés conducir")
    