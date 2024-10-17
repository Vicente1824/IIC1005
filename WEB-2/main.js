for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) {
    console.log(i)
  }
}

let boton_generar = document.getElementById('boton-generar-CV')
boton_generar.addEventListener('click', generar_cv)
let boton_validar_mail = document.getElementById('boton-validar-mail')
boton_validar_mail.addEventListener('click', validar_mail)

function generar_cv() {
    cambiar_nombre()
    cambiar_apellido()
    cambiar_titulo()
    cambiar_celular()
    cambiar_email()
    cambiar_ubicacion()
    cambiar_perfil()
    cambiar_trabajo_institucion()
    cambiar_input_trabajo_1()
    cambiar_input_trabajo_2()
    cambiar_estudios_institucion()
    cambiar_estudios_1()
    cambiar_estudios_2()
    cambiar_idioma_1()
    cambiar_idioma_2()
}

function cambiar_nombre() {
    let nombre = document.getElementById('input-nombre').value
    document.getElementById('nombre').innerHTML = nombre
}

function cambiar_apellido() {
    let apellido = document.getElementById('input-apellido').value
    document.getElementById('apellido').innerHTML = apellido
}

function cambiar_titulo() {
    let titulo = document.getElementById('input-titulo').value
    document.getElementById('titulo').innerHTML = titulo
}

function cambiar_celular() {
    let celular = document.getElementById('input-celular').value
    document.getElementById('celular').innerHTML = celular
}

function cambiar_email() {
    let email = document.getElementById('input-email').value
    document.getElementById('email').innerHTML = email
}

function cambiar_ubicacion() {
    let ubicacion = document.getElementById('input-ubicacion').value
    document.getElementById('ubicacion').innerHTML = ubicacion
}

function cambiar_perfil() {
    let perfil = document.getElementById('input-perfil').value
    document.getElementById('perfil').innerHTML = perfil
}

function cambiar_trabajo_institucion() {
    let trabajo = document.getElementById('input-trabajo-institucion').value
    document.getElementById('trabajo-institucion').innerHTML = trabajo
}

function cambiar_input_trabajo_1() {
    let trabajo = document.getElementById('input-trabajo-1').value
    document.getElementById('trabajo-1').innerHTML = trabajo
}

function cambiar_input_trabajo_2() {
    let trabajo = document.getElementById('input-trabajo-2').value
    document.getElementById('trabajo-2').innerHTML = trabajo
}

function cambiar_estudios_institucion() {
    let estudios = document.getElementById('input-estudios-institucion').value
    document.getElementById('estudios-institucion').innerHTML = estudios
}

function cambiar_estudios_1() {
    let estudios = document.getElementById('input-estudios-1').value
    document.getElementById('estudios-1').innerHTML = estudios
}

function cambiar_estudios_2() {
    let estudios = document.getElementById('input-estudios-2').value
    document.getElementById('estudios-2').innerHTML = estudios
}

function cambiar_idioma_1() {
    let idioma = document.getElementById('input-idioma-1').value
    document.getElementById('idioma-1').innerHTML = idioma
}

function cambiar_idioma_2() {
    let idioma = document.getElementById('input-idioma-2').value
    document.getElementById('idioma-2').innerHTML = idioma
}

function validar_mail() {
    let email = document.getElementById('input-email').value
    let correcto = email.slice(-6)
    if (correcto === '@uc.cl') {
        console.log('True')
    }
    else {
        console.log('False')
    }
}