let user = "admin"
let password = "admin"

// let userVal = prompt('Insira o usuario')
// let passVal = prompt('Insira a senha')

let trys = 3
let ver = false

while (trys!=0) {
    let userVal = prompt('Insira o usuario')
    let passVal = prompt('Insira a senha')

    if(userVal === userVal && passVal === password) {
        alert("Logado com sucesso")
    } else {
        alert('Usuario ou senha incorretos')
        trys = trys - 1
    }
}
console.log(trys)
if(trys === 0) {
    alert('Suas tentativas acabaram')
}


// Exercicio 01

/* if(userVal === userVal && passVal === password) {
    alert("Logado com sucesso")
} else {
    alert("Usuario ou senha incorretos")
} */