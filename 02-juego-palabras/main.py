import random

words = [
    "casa", "rojo", "sol", "flor", "luz",
    "agua", "tiempo", "música", "gato", "mesa",
    "cielo", "puerta", "libro", "fuego", "viento",
    "azul", "piedra", "nieve", "hoja", "risa",
    "ciudad", "aire", "papel", "sonrisa", "nube",
    "tren", "silla", "luna", "naranja", "cuerpo",
    "pueblo", "noche", "niebla", "frío", "verde",
    "piedra", "ojo", "amor", "brazo", "boca",
    "número", "puente", "café", "lengua", "pelo",
    "fruta", "trabajo", "río", "cuerda", "mano",
    "ventana", "campo", "lago", "idea", "paso",
    "vuelo", "mes", "punto", "corazón", "nombre",
    "colores", "camino", "caballo", "dientes", "carne",
    "silencio", "cabeza", "cama", "animal", "hombro",
    "ciencia", "dedos", "ojos", "pantalla", "alma",
    "oreja", "guitarra", "regla", "flor", "sendero",
    "lápiz", "historia", "niños", "dedo", "ratón",
    "luz", "mente", "verano", "piso", "hoja",
    "amigo", "línea", "sabor", "brazo", "barco",
    "mesa", "espejo", "forma", "miedo", "pared"
]

def juego(palabra):
  barras = ""
  atempts = 10
  
  for i in range(len(palabra)):
    barras += "_"
  
  print("Bienvenido al juego")
  print(f"La palabra tiene {len(palabra)} letras")
  
  while atempts > 0:

    print(f"\nPalabra: {barras}")
    letraEscogida = input("Cual es la letra: ").lower()
 
    adivinado = False
    
    posicion = 0
    
    ganado = False
    
    for letra in palabra:
      if letra == letraEscogida:

        print("Letra adivinada")
        adivinado = True
        
        posicion = palabra.index(letra)
        
        lista_barras = list(barras)
        lista_barras[posicion] = letra
        
        barras = ''.join(lista_barras)

        if(barras == palabra):
          ganado = True
      elif ganado == True:
        break

    if ganado == True:
      print("\nHas ganado")
      break

    if adivinado == False:
      print("Has fallado")
      atempts -= 1
      
    if atempts == 0:
      print("\nHas perdido")
      print(f"La palabra era: {palabra}")      
    
juego(random.choice(words))