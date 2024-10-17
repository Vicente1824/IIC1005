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

class CV(BaseModel):
    nombre: str
    titulo: str
    celular: str
    email: str
    trabajo_institucion: str
    estudios_institucion: str

@app.get("/first-curriculum")
def give_first_curriculum():
    with open("curriculums.txt", "r", encoding = "utf-8") as archivo:
        info = archivo.readlines()
    info = info[0].strip().split(";")
    cv_pedido = {}
    cv_pedido["nombre"] = f"{info[0]} {info[1]}"
    cv_pedido["titulo"] = info[2]
    cv_pedido["celular"] = info[3]
    cv_pedido["email"] = info[4]
    cv_pedido["trabajo_institucion"] = info[5]
    cv_pedido["estudios_institucion"] = info[6]
    return cv_pedido

@app.get("/name-curriculums")
def conseguir_nombres() -> list:
    with open('curriculums.txt', 'r', encoding = "utf-8") as archivo:
        lista_nombres = []
        for linea in archivo:
           lista =  linea.split(";")
           lista_nombres.append(lista[0])
    return lista_nombres

@app.get("/curriculum/{nombre}")
def conseguir_cv(nombre):
    with open('curriculums.txt', 'r', encoding = "utf-8") as archivo:
        for linea in archivo:
            lista =  linea.split(";")
            if lista[0] == nombre:
                diccionario = {"nombre": f"{lista[0]} {lista[1]}", "titulo": lista[2],
                               "celular": lista[3], "email": lista[4],
                               "trabajo_institucion": lista[5], "estudios_institucion": lista[6]}
                return diccionario
    return "ERROR NO ENCONTRÉ NADA"

@app.get("/curriculum/{nombre}")
def give_curriculum(nombre: str):
    archivo = open("curriculums.txt", encoding="utf-8")
    informacion = archivo.readlines()
    for i in range(len(informacion)):
        cv = informacion[i].strip().split(";")
        if cv[0] == nombre:
            cv_a_entregar = {}
            cv_a_entregar["nombre"] = cv[0]
            cv_a_entregar["apellido"] = cv[1]
            cv_a_entregar["titulo"] = cv[2]
            cv_a_entregar["celular"] = cv[3]
            cv_a_entregar["email"] = cv[4]
            cv_a_entregar["trabajo_institucion"] = cv[5]
            cv_a_entregar["estudios_institucion"] = cv[6]
            return cv_a_entregar

@app.post("/curriculum")
def create_curriculum(cv:CV):
    archivo = open("curriculums.txt", "a", encoding="utf-8")
    nombre=(cv.nombre.split(" ")[0])
    apellido=(cv.nombre.split(" ")[1])
    titulo=cv.titulo
    celular=cv.celular
    email=cv.email
    trabajo_institucional=cv.trabajo_institucional
    estudios_institucion=cv.estudios_institucion
    texto=nombre+";"+apellido+";"+titulo+";"+celular+";"+email+";"+trabajo_institucional+";"+estudios_institucion
    print(texto, file=archivo)
    archivo.close()

lista_atributos = list(CV.__annotations__.keys())