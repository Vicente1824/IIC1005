async function crearUsuario() {
    const data = {
        username: obtenerInput("username-registro"),
        nombre: obtenerInput("nombre"),
        apellido: obtenerInput("apellido"),
        correo: obtenerInput("correo"),
        contrasena: obtenerInput("contrasena-registro"),
    }

    const response = await fetch("http://127.0.0.1:8000/usuario", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });
    if (response.ok) {
        alert("Usuario creado exitosamente")
    } else {
        alert("Error al registrarte")
    }
}

async function verificarUsuario() {
    const username = obtenerInput("username-inicio")
    const contrasena = obtenerInput("contrasena-inicio")
    const response = await fetch(`http://127.0.0.1:8000/usuario/${username}-${contrasena}`, {
        method: "GET",
        headers: {
            'Content-Type': 'application/json',
        },
    });
    if (response.ok) {
        const respuesta = await response.json();
        if (respuesta) {
            alert("Usuario encontrado, iniciando sesión...")
            await obtenerNombre(username)
            window.location.href = "feed.html"
        }
        else {
            alert("Usuario no encontrado o contraseña incorrecta.")
        }
    } else {
        alert("Error desconocido.")
    }
}

function obtenerInput(nombre) {
    return document.getElementById(nombre).value
}

function cambiarTags(username, nombre) {
    alert("Cambiando tags")
    cambiarTagRequest("titulo-barra-lateral", username)
    cambiarTagRequest("subtitulo-barra-lateral", nombre)
}


function cambiarTagRequest(nombre, data) {
    const elemento_a_cambiar = document.getElementById(nombre)
    elemento_a_cambiar.innerHTML = data[nombre];
}

async function obtenerNombre(username) {
    const response = await fetch(`http://127.0.0.1:8000/usuario/${username}`, {
        method: "GET",
        headers: {
            'Content-Type': 'application/json',
        },
    });
    if (response.ok) {
        const respuesta = await response.json();
        localStorage.setItem('nombre', respuesta.nombre);
        localStorage.setItem('username', respuesta.username);
    } else {
        alert("Error");
    }
}

document.getElementById("boton-registro").addEventListener("click", crearUsuario)
document.getElementById("boton-inicio").addEventListener("click", verificarUsuario)