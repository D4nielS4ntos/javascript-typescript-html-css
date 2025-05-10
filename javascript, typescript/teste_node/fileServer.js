const http = require('http');
const url = require('url');
const fs = require('fs');
// const uc = require('upper-case');

const server = http.createServer((req, res) => {
    try {
        const q = url.parse(req.url, true);
        const filename = "." + q.pathname;
        fs.readFile(filename, (err, data) => {
            if (err) {
                res.writeHead(404, {'Content-Type': 'text/html'});
                return res.end("404 Not Found");
            }
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            return res.end();
        });
    } catch (error) {
        console.error(error);
        return res.end("erro: " + error);
    }
});

server.listen(3000, () => {
    console.log('Servidor está rodando na porta 3000');
});
