import time

def comprobador():

  contraseña = input("\nContraseña a comprobrar: ")

  while True:

    insegura = False
    
    mayus = 0
    
    minus = 0
    
    num = 0
        
    if len(contraseña) < 8:
      insegura = True
    
    for letra in contraseña:

      if letra.isupper():
        mayus += 1

      elif letra.islower():
        minus += 1
        
      try :
        i = int(letra)
        
        num += 1
      except ValueError: num = num 

    if insegura == True:
      print("\nEs demasiado corta")
      comprobador()
      break

    elif mayus < 2:
      print("Tiene menos de 2 mayusculas")
      comprobador()
      break

    elif minus < 2:
      print("Tiene menos de 2 minusculas")
      comprobador()
      break

    elif num < 2:
      print("Tiene menos de 2 numeros")
      comprobador()
      break
    
    else:
      print("\nEs segura")
      break
    

print("Bienvenido al comprobador de seguridad de contraseñas")
time.sleep(0.5)

print("\nCargando...")
time.sleep(1.5)

comprobador()