class Pessoa {
    nome:string
    cpf:string
    idade:number

    constructor(nome, cpf, idade) {
        this.nome = nome
        this.cpf = cpf
        this.idade = idade
    }

    retornarInformacoes() {
        return [this.nome, this.cpf, this.idade]
    }
}

const Vitor = new Pessoa("Vitor", "000.000.000-00", 18)
const Sara = new Pessoa("Sara", "111.111.111-11", 17)

console.log(Vitor)
console.log(Sara)