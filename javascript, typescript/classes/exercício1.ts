class Livro {
    nome:string
    genero:string
    numeroPaginas:number
    autor:string

    constructor(nome, genero, numeroPaginas, autor) {
        this.nome = nome
        this.genero = genero
        this.numeroPaginas = numeroPaginas
        this.autor = autor
    }

    retornarInformacoes() {
        return [this.nome, this.genero, this.numeroPaginas, this.autor]
    }
}

class Turma {
    nome:string
    alunos:string[]
    professores:string[]

    constructor(nome, alunos, professores) {
        this.nome = nome
        this.alunos = alunos
        this.professores = professores
    }

    retornarInformacoes() {
        return [this.nome, this.alunos, this.professores]
    }
}

class Estudante {
    nomeCompleto:string
    idade:number
    turma:string

    constructor(nomeCompleto, idade, turma) {
        this.nomeCompleto = nomeCompleto
        this.idade = idade
        this.turma = turma
    }

    retornarInformacoes() {
        return [this.nomeCompleto, this.idade, this.turma]
    }
}
