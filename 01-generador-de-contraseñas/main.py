import random
import time


def generar(lon):
  caracteres = "abcdefghijklmnñopqrstuvwxyz1234567890_-!@#$%&/()=[]"

  i = 0
  
  contraseña = ''

  while i < lon:
    contraseña += ''.join(random.choice(caracteres))
    i += 1
  return contraseña

lon = int(input("Longitud de la contraseña: "))

time.sleep(0.5)

print("\nGenerando contraseña...")

time.sleep(2)  
  
print(f"\nLa contraseña es: {generar(lon)}")  