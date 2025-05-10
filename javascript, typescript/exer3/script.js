
function mostrarResultado() {
    let inicio = document.querySelector('input#txtinicio')
    let fim = document.querySelector('input#txtfim')
    let progressao = document.querySelector('input#txtprog')
    let res = document.querySelector('div#res')

    
    if (inicio.value.length == 0 || fim.value.length == 0 || progressao.value.length == 0) {
        alert('[ERRO] Faltam dados')
        res.innerText = 'Impossível contar!'
    } else {
        res.innerHTML = `Contando: <br>`
        let contador = Number(inicio.value)
        let final = Number(fim.value)
        let prog = Number(progressao.value)

        if (prog < 1) {
            res.innerHTML += 'Progressão inválida. O valor será considerado como 1: <br>'
            prog = 1
        }
        if (contador < final) {
            for(contador; contador <= final; contador += prog) {
                res.innerText += ` ${contador} \u{1F449} `
            }
        } else if (contador > final) {  
            for(contador; contador >= final; contador -= prog) {
                res.innerText += ` ${contador} \u{1F449} `
            }
        }
        res.innerText += `\u{1F6A9}`
    }
}
