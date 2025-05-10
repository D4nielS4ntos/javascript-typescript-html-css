const http = require("http");
const fs = require("fs");
const mysql = require("mysql");
const formidable = require("formidable");

// Configuração do banco de dados
const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    // password: "sua_senha",
    database: "ex_guardar_arquivo"
});

db.connect((err) => {
    if (err) throw err;
    console.log("Conectado ao MySQL!");
});

// Criando o servidor HTTP
const server = http.createServer((req, res) => {
    // POST
    if (req.method === "POST" && req.url === "/upload") {
        const form = new formidable.IncomingForm();
        form.parse(req, (err, fields, files) => {
            if (err) {
                res.writeHead(400, { "Content-Type": "text/plain" });
                res.end("Erro ao processar o arquivo.");
                return;
            }

            const file = files.arquivo;
            fs.readFile(file.filepath, (err, data) => {
                if (err) {
                    res.writeHead(500, { "Content-Type": "text/plain" });
                    res.end("Erro ao ler o arquivo.");
                    return;
                }

                const sql = "INSERT INTO imagens (nome, tipo, arquivo) VALUES (?, ?, ?)";
                db.query(sql, [file.originalFilename, file.mimetype, data], (err, result) => {
                    if (err) {
                        res.writeHead(500, { "Content-Type": "text/plain" });
                        res.end("Erro ao salvar no banco.");
                        return;
                    }

                    res.writeHead(200, { "Content-Type": "text/plain" });
                    res.end("Imagem enviada com sucesso!");
                });
            });
        });
    } 
    // GET
    else if (req.method === "GET" && req.url.startsWith("/imagem/")) {
        // const id = req.url.split("/")[2];
        const sql = "SELECT * FROM imagens_blob";

        db.query(sql, [], (err, result) => {
            if (err || result.length === 0) {
                res.writeHead(404, { "Content-Type": "text/plain" });
                res.end("Imagem não encontrada.");
                return;
            }

            res.writeHead(200, { "Content-Type": result[0].tipo });
            res.end(result[0].arquivo);
        });
    } 
    // EXCESÃO
    else {
        res.writeHead(404, { "Content-Type": "text/plain" });
        res.end("Rota não encontrada.");
    }
});

// Iniciando o servidor
server.listen(3000, () => {
    console.log("Servidor rodando em http://localhost:3000");
});
