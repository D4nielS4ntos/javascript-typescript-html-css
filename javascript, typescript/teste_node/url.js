const http = require('http');
const url = require('url');

const server = http.createServer((req, res) => {
    try {
        const adress = 'local://localhost:3000/default.htm?year=333&month=abril';//req.url;
        res.writeHead(200, {'Content-Type': 'text/html'});
        // console.log(adress);
        const q = url.parse(adress, true);
        res.write("<br>mensagem: " + req.headers.host + req.url);
        res.write("<br>mensagem: " + q.scheme);
        res.write("<br>mensagem: " + q.host);
        res.write("<br>mensagem: " + q.hostname);
        res.write("<br>mensagem: " + q.port);
        res.write("<br>mensagem: " + q.pathname);
        res.write("<br>mensagem: " + q.search);
        res.write("<br>mensagem: " + JSON.stringify(q.query));
        res.write("<br>mensagem: " + q.query.year + " " + q.query.month);
        res.end();
    } catch (error) {
        console.error(error);
        res.end("erro: " + error);
    }
});

const PORT = 3000;

server.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
});
