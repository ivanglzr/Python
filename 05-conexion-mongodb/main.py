from pymongo import MongoClient

client = MongoClient("localhost")

db = client["python"]

col = db["users"]

print("Que quieres hacer: \n 1. Crear usuario \n 2. Editar usuario \n 3. Eliminar usuario")
op = int(input(""))

if op == 1:
  name = input("Name: ")
  email = input("Email: ")
  password = input("Password: ")

  col.insert_one({
    "name": name,
    "email": email,
    "password": password
  })

elif op == 2:
  id = input("Id: ")

  name = input("Name: ")
  email = input("Email: ")
  password = input("Password: ")

  col.update_one({ "_id": id}, {
      "name": name,
      "email": email,
      "password": password
  })

elif op == 3:
  id = input("Id: ")

  col.delete_one({ "_id": id})
  
else: 
  print("Opcion incorrecta")