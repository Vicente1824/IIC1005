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

"""@app.get("/name-curriculums")
def give_name():
    archivo = open("curriculums.txt", encoding="utf-8")
    informacion = archivo.readlines()
    nombres = []
    for i in range(len(informacion)):
        nombre = informacion[i].split(";")[0]
        nombres.append(nombre)
    return nombres

@app.get("/first-curriculum")
def give_curriculum():
    archivo = open("curriculums.txt", encoding="utf-8")
    informacion = archivo.readlines()
    primer_cv = informacion[0].strip().split(";")
    cv_a_entregar = {}

    cv_a_entregar["nombre"] = primer_cv[0]
    cv_a_entregar["titulo"] = primer_cv[1]
    cv_a_entregar["celular"] = primer_cv[2]
    cv_a_entregar["email"] = primer_cv[3]
    cv_a_entregar["trabajo_institucion"] = primer_cv[4]
    cv_a_entregar["estudios_institucion"] = primer_cv[5]

    return cv_a_entregar
"""
@app.get("/usuario/{username}")
def dar_usuario(username: str):
    archivo = open("usuarios.txt", encoding="utf-8")
    informacion = archivo.readlines()
    for i in range(len(informacion)):
        usuario = informacion[i].strip().split(";")
        if usuario[0] == username:
            usuario_a_entregar = {}
            usuario_a_entregar["username"] = usuario[0]
            usuario_a_entregar["nombre"] = usuario[1]
            usuario_a_entregar["apellido"] = usuario[2]
            usuario_a_entregar["correo"] = usuario[3]
            usuario_a_entregar["contrasena"] = usuario[4]
            archivo.close()
            return usuario_a_entregar

@app.post("/usuario")
def crear_usuario(usuario: Usuario):
    archivo = open("usuarios.txt", "a", encoding="utf-8")
    print("hola", file=archivo)
    nombre = usuario.nombre
    apellido = usuario.apellido
    username = usuario.username
    correo = usuario.correo
    contrasena = usuario.contrasena
    texto = f"{nombre};{apellido};{username};{correo};{contrasena};"
    print(texto, file=archivo)
    archivo.close()




