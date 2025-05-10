
function verificar() {
    let data = new Date()
    let ano = data.getFullYear()
    let fano = document.querySelector('input#txtano')
    let res = document.querySelector('div#res')

    if (fano.value.length == 0 || Number(fano.value) > ano) {
        alert('[ERRO]')
    } else {
        let fsex = document.getElementsByName('radsex')
        let idade = ano - Number(fano.value)
        let genero = ``
        let img = document.createElement('img')
        img.setAttribute('id', 'foto')

        if (fsex[0].checked) {
            genero = `homem`
            if (idade >=0 && idade <= 10) {
                img.setAttribute('src', `img/criançaM.webp`)
            } else if (idade > 10 && idade <= 20) {
                img.setAttribute('src', `img/jovemM.webp`)
            } else if (idade > 20 && idade <= 60) {
                img.setAttribute('src', `img/adultoM.jpeg`)        
            } else if (idade > 60) {
                img.setAttribute('src', `img/idosoM.jpeg`)
            }
        } else if (fsex[1].checked) {
            genero = `mulher`
            if (idade >=0 && idade <= 10) {
                img.setAttribute('src', `img/criançaF.webp`)
            } else if (idade > 10 && idade <= 20) {
                img.setAttribute('src', `img/jovemF.jpeg`)
            } else if (idade > 20 && idade <= 60) {
                img.setAttribute('src', `img/adultoF.jpeg`)        
            } else if (idade > 60) {
                img.setAttribute('src', `img/idosoF.webp`)
            }
        } else {
            `[ERRO]`
        }
        res.innerHTML = `É ${genero} com idade calculada de ${idade} anos.`
        res.appendChild(img)
    }
}
