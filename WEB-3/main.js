async function crearCV() {
    const data = {
        nombre: obtenerInput("nombre"),
        titulo: obtenerInput("titulo"),
        celular: obtenerInput("celular"),
        email: obtenerInput("email"),
        trabajo_institucion: obtenerInput("trabajo-institucion"),
        estudios_institucion: obtenerInput("estudios-institucion"),
    }

    const response = await fetch("http://127.0.0.1:8000/curriculum", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (response.ok) {
        alert("CV Creado exitosamente")
    } else {
        alert("Error al crear el CV")
    }
}

function obtenerInput(nombre) {
    return document.getElementById(`input-${nombre}`).value
}

function obtenerCV() {
    const nombre = document.getElementById(`input-nombre-a-buscar`).value

    fetch(`http://127.0.0.1:8000/curriculum/${nombre}`)
        .then(response => {
            if (response.status == 405) {
                alert("Error 405: No se ha entregado ningun parametro")
            }
            return response.json()
        })
        .then(data => {
            cambiarTagsRequest(data)
        })
        .catch(error => {
            alert(error)
        });
}

function obtenerPrimerCV() {
    fetch(`http://127.0.0.1:8000/first-curriculum`)
        .then(response => {
            if (response.status == 405) {
                alert("Error 405: No se ha entregado ningun parametro")
            }
            return response.json()
        })
        .then(data => {
            cambiarTagsRequest(data)
        })
        .catch(error => {
            alert(error)
        });
}

function cambiarTagsRequest(data) {
    cambiarTagRequest("nombre", data)
    cambiarTagRequest("titulo", data);
    cambiarTagRequest("celular", data);
    cambiarTagRequest("email", data);
    cambiarTagRequest("trabajo_institucion", data);
    cambiarTagRequest("estudios_institucion", data);
}

async function obtenerTodosLosCV() {
    fetch(`http://127.0.0.1:8000/name-curriculums`)
        .then(response => {
            if (response.status == 405) {
                alert("Error 405: No se ha entregado ningun parametro")
            }
            return response.json()
        })
        .then(data => {
            alert(data)
        })
        .catch(error => {
            alert(error)
        });
}

function cambiarTagRequest(nombre, data) {
    const elemento_a_cambiar = document.getElementById(nombre)
    elemento_a_cambiar.innerHTML = data[nombre];
}

document.getElementById("boton-generar-CV").addEventListener("click", crearCV)
document.getElementById("boton-obtener-nombres").addEventListener("click", obtenerTodosLosCV)
document.getElementById("boton-primer-cv").addEventListener("click", obtenerPrimerCV)
document.getElementById("boton-obtener-cv").addEventListener("click", obtenerCV)