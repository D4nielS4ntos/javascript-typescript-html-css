
function addTabuada() {
    let numero = document.querySelector('input#txtnum')
    let textarea = document.querySelector('select#tabuada')

    if (numero.value.length == 0) {
        return
    } else {
        textarea.innerHTML = 'Resultado:'
        
        for (let x = 1; x <= 10; x++) {
            let item = document.createElement('option')
            item.text = `${numero.value} x ${x} = ${numero.value * x}`
            item.value = `tab${x}`
            textarea.appendChild(item)
            textarea.size = x
        }
    }
}
