from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Usuario(BaseModel):
    username: str
    nombre: str
    apellido: str
    correo: str
    contrasena: str

lista_atributos = list(Usuario.__annotations__.keys())

@app.get("/usuario/{username}-{contrasena}")
def dar_usuario(username: str, contrasena: str):
    archivo = open("usuarios.txt", "r", encoding="utf-8")
    informacion = archivo.readlines()
    archivo.close()
    for i in range(len(informacion)):
        usuario = informacion[i].strip().split(";")
        if usuario[0] == username:
            if contrasena == usuario[4]:
                return True
            else:
                return False
    return False

@app.post("/usuario")
def crear_usuario(usuario: Usuario):
    archivo = open("usuarios.txt", "a", encoding="utf-8")
    nombre = usuario.nombre
    apellido = usuario.apellido
    username = usuario.username
    correo = usuario.correo
    contrasena = usuario.contrasena
    texto = f"{username};{nombre};{apellido};{correo};{contrasena}"
    print(texto, file=archivo)
    archivo.close()

@app.get("/usuario/{username}")
def dar_nombre(username: str):
    archivo = open("usuarios.txt", "r", encoding="utf-8") 
    informacion = archivo.readlines()
    archivo.close()
    for i in range(len(informacion)):
        usuario = informacion[i].strip().split(";")
        if usuario[0] == username:
            return {"nombre": f"{usuario[1]} {usuario[2]}", "username": usuario[0]}
    return None


