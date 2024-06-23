
let itensList = []
let resultados = document.querySelector('div#resultados')

a()

function checkList() {
    for (x in itensList) {
        if (itensList[x] == num) {
            alert('Este número já está na lista')
            return true
        }
    }
}


function checarSeEntreLimite(numero) {
    if (numero.value.length == 0) {
        alert('O valor não pode ser vazio!')
        return
    }
    if (num >= 1 && num <= 100) {
        return true
    } else {
        alert('O numero precisa ser entre 1 e 100')
    }
}


function addNumero() {
    let numero = document.querySelector('input#txtnum')
    let textarea = document.querySelector('select#numeros')
    num = Number(numero.value)
    resultados.innerHTML = ''

    if (!checkList() && checarSeEntreLimite(numero)) {
        let item = document.createElement('option')
        item.text = `Valor ${num} adicionado`
        
        itensList.push(num)
        textarea.appendChild(item)
        textarea.size = itensList.length
    }
}


function mostrarResultados() {
    let itensListCopy = [...itensList]
    let soma = 0
    let media = 0

    if (itensListCopy.length == 0) {
        alert('Preencha algum número antes de ver o resultado.')
        return
    }

    for (x in itensListCopy) {
        soma += itensListCopy[x]
    }
    media = soma / itensList.length

    resultados.innerHTML = ''
    resultados.innerHTML += `<p>Ao todo, temos ${itensListCopy.length} números cadastrados.</p>`
    resultados.innerHTML += `<p>O maior valor foi ${Math.max(...itensListCopy)}.</p>`
    resultados.innerHTML += `<p>O menor valor informado foi ${Math.min(...itensListCopy)}.</p>`
    resultados.innerHTML += `<p>A soma de todos os valores foi ${soma}.</p>`
    resultados.innerHTML += `<p>A média do valores digitados foi ${media}.</p>`
}
