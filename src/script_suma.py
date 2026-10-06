import random

# Generamos dos números aleatorios para la prueba automática
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
suma = num1 + num2

resultado_texto = f"Número 1: {num1} + Número 2: {num2} = Suma total: {suma}\n"

# Guarda el resultado en un archivo de texto
with open("resultado.txt", "a") as f:
    f.write(resultado_texto)

print(f"¡Suma realizada con éxito! {resultado_texto.strip()}")