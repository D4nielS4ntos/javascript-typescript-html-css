// import { a } from "./modulo.js"
// import a from "./modulo.js"
import * as a from "./modulo.js"

function f_a() {
    alert(a.a)
}
alert(a.a)

document.querySelector('button').addEventListener('click', (event) => f_a())