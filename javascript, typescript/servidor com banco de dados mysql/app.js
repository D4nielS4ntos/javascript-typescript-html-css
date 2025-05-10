const express = require('express')
const cors = require('cors')
const path = require('path')
const app = express()
const cadastroRouter = require('./controller.js')

// app.use(express.json())
// app.use(cors())

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, '/index.html')) 
})

app.use("/cadastro", cadastroRouter)

app.listen(3000, () => {
    console.log(`Servidor express rodando...`)
})
