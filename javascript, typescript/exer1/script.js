
function carregar() {
    let msg = window.document.getElementById('msg')
    let img = document.getElementById('imagem')
    let data = new Date()
    let hora = data.getHours()
    let body = window.document.querySelector('body')
    msg.innerHTML = `Agora são ${hora} horas.`
    
    if (hora >= 0 && hora < 8) {
        img.src = 'img/manhã.jpg'
        body.style.backgroundColor = '#5099C4'
    } else if (hora >= 8 && hora < 16) {
        img.src = 'img/tarde.jpeg'
        body.style.backgroundColor = '#3482AC'
    } else if (hora >= 16 && hora < 18) {
        img.src = 'img/anoitecer.webp'
        body.style.backgroundColor = '#F66400'
    } else if (hora >= 18 && hora < 24) {
        img.src = 'img/noite.jpeg'
        body.style.backgroundColor = '#162F4B'
    }
}