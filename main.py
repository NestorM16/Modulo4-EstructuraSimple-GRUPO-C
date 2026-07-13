# Información del usuario
nombre = input("Por favor, ingresa tu nombre: ")
edad = int(input("Por favor, ingresa tu edad: "))
ciudad = input("Por favor, ingresa tu ciudad: ")

# Mensaje principal
print("\n¡Hola,", nombre + "! Tienes", edad, "años y vives en", ciudad + ".\n")

# Continuación de la historia
comida = input("¿Cuál es tu comida favorita?: ")
lenguaje = input("¿Qué lenguaje de programación te gustaría aprender?: ")

print(
    f"\nUn día, {nombre} decidió comenzar a estudiar programación en {ciudad}.\n"
    f"Antes de empezar, comió {comida} para tener energía.\n"
    f"Luego abrió su computadora y empezó a aprender {lenguaje}.\n"
    f"Después de practicar durante varias horas, logró crear su primer programa y terminó el día muy feliz."
)