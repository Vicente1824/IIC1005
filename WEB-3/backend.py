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

lista_atributos = list(CV.__annotations__.keys())


@app.get("/")
def hello_world():
    return "Hello World"

@app.get("/name-curriculums")
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
    trabajo_institucion=cv.trabajo_institucion
    estudios_institucion=cv.estudios_institucion
    texto=nombre+";"+apellido+";"+titulo+";"+celular+";"+email+";"+trabajo_institucion+";"+estudios_institucion
    print(texto, file=archivo)
    archivo.close()




