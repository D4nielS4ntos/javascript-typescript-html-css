const http = require('http');
const fs = require('fs');
const path = require('path');

// const express = require('express');
// const app = express();

const server = http.createServer((req, res) => {
    // Configura os cabeçalhos para habilitar CORS
    res.setHeader('Access-Control-Allow-Origin', '*'); // Pode substituir '*' por um domínio específico, ex: 'http://localhost:5500'
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS'); // Métodos permitidos
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type'); // Cabeçalhos permitidos

    if (req.method.toUpperCase() === 'GET' && req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
        res.write("<h1>Olá Mundo</h1>");
        res.end();
    } else if (req.method.toUpperCase() === 'GET' && req.url === '/imagem') {
        const file = path.join(__dirname, 'imagens', 'Captura de Tela (144).png');
        const fileStream = fs.createReadStream(file);
        res.writeHead(200, { 'Content-Type': 'image/png;charset=utf-8' });
        fileStream.pipe(res);
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('Página não encontrada!');
    }
});

const port = 3000;

server.listen(port, () => {
    console.log('Server rodando na porta: ' + port);
});
