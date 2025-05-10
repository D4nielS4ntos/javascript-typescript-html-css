const http = require('http');
const url = require('url');
const hwModule = require('./modulohelloworld');

const server = http.createServer((req, res) => {
    try {
        res.writeHead(200, {'Content-Type': 'text/html'});
        const q = url.parse(req.url, true).query;
        console.log(req.url);
        // console.log(q.year + " " + q.month);
        // res.end("mensagem: " + hwModule.helloWorld());
        res.end("mensagem: " + hwModule.helloWorld() + "<br>" + q.year + " " + q.month);
    }
    catch (error) {
        console.error(error);
        res.end("erro: " + error);
    }
});

const PORT = 3000;

server.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
});
