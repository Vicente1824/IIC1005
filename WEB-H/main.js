async function crearUsuario() {
    const data = {
        username: obtenerInput("username"),
        nombre: obtenerInput("nombre"),
        apellido: obtenerInput("apellido"),
        correo: obtenerInput("correo"),
        contrasena: obtenerInput("contrasena"),
    }

    const response = await fetch("http://127.0.0.1:5500/usuario", {
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

function obtenerInput(nombre) {
    return document.getElementById(nombre).value
}


function cambiarTagsRequest(data) {
    cambiarTagRequest("nombre", data)
    cambiarTagRequest("titulo", data);
    cambiarTagRequest("celular", data);
    cambiarTagRequest("email", data);
    cambiarTagRequest("trabajo_institucion", data);
    cambiarTagRequest("estudios_institucion", data);
}


function cambiarTagRequest(nombre, data) {
    const elemento_a_cambiar = document.getElementById(nombre)
    elemento_a_cambiar.innerHTML = data[nombre];
}

document.getElementById("boton-registro").addEventListener("click", crearUsuario)