const fs = require('fs');
const path = require('path');

const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(cors({
    origin: 'http://localhost:5500',
    methods: ["GET", "POST", "PUT", "DELETE"]
}));

app.get('/', (req, res) => {
    res.send("<h1>Olá Mundo</h1>");
});

app.get('/imagem', (req, res) => {
    const filePath = path.join(__dirname, 'imagens', 'Touhou_Bad_Apple.mp4');
    // res.sendFile(filePath);
    const fileStream = fs.createReadStream(filePath);
    fileStream.pipe(res);
});

app.get('/imagem/:nome', (req, res) => {
    try {
        const { nome } = req.params;
        const filePath = path.join(__dirname, 'imagens', nome);
        const fileStream = fs.createReadStream(filePath);
        fileStream.pipe(res);
        // res.send(nome);
    } catch (error) {
        res.status(500).send(error.message);
    }
});

app.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
});
