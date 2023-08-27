import time as time

print("Bienvenido a la calculadora \n")
time.sleep(1)

print("Cargando... \n")
time.sleep(1.5)

print("Que quieres hacer: \n" "Suma \n" "Resta \n" "Multiplicacion \n" "Division \n")

op = input()
op = op.lower()

num1 = float(input("\nCual es el primer numero: ")) 
num2 = float(input("Cual es el segundo numero: "))

if op == "suma":
  print(f"\nEl resultado es: {num1 + num2}")
elif op == "resta":
  print(f"\nEl resultado es: {num1 - num2}")
elif op == "multiplicacion":
  print(f"\nEl resultado es: {num1 * num2}")
elif op == "division":
  print(f"\nEl resultado es: {num1 / num2}")
else:
  print("No se ha encontrado la operacion")