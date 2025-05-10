const express = require('express')
const router = express.Router()
const db = require('./util/db')

/**
 * Executa uma consulta no banco de dados e envia uma resposta.
 * @param {string} sql - A consulta SQL a ser executada.
 * @param {Array} params - Os parâmetros para a consulta SQL.
 * @param {Object} res - O objeto de resposta do Express.
 * @param {string} erroMsg - Mensagem de erro para ser enviada em caso de falha.
 */

// class cadastroControler {
//   constructor(db, router) {
//     this.db = db
//     this.router = router
//   }

//   a() {
//     let aaa = 'aaaaaaaaaaaaaaaaaaaaaaa'
//     return aaa
//   }

//   executarConsulta(sql, params, res, erroMsg) {
//     return new Promise((resolve, reject) => {
//       db.query(sql, params, (err, result) => {
//         if (err) {
//           // res.status(500).json({ erro: erroMsg, detalhes: err });
//           console.log('erro')
//           reject(err)
//         } else {
//           // res.status(200).json(result);
//           console.log('show')
//           resolve(result)
//         }
//       });
//     })
//   }

//   pegarCadastro(){
//     router.get('/cadastro', (req, res) => {
//       executarConsulta('SELECT * FROM tbteste', [], res, "Erro na consulta de tbteste");
//     )}
//   }
// }

function executarConsulta(sql, params, res, erroMsg) {
    db.query(sql, params, (err, result) => {
      if (err) {
        res.status(500).json({ erro: erroMsg, detalhes: err })
      } else {
        res.status(200).json(result)
      }
    })
}


router.get('/', (req, res) => {
    executarConsulta('SELECT * FROM tbteste', [], res, "Erro na consulta de tbteste")
})

module.exports = router
