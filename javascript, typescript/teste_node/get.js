const http = require("http");
const mysql = require("mysql");

// Configuração do banco de dados
const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    // password: "sua_senha",
    database: "ex_biblioteca"
});

db.connect((err) => {
    if (err) throw err;
    console.log("Conectado ao MySQL!");
});

// Criando o servidor HTTP
const server = http.createServer((req, res) => {
    if (req.method === "GET") {
        const sql = "SELECT * FROM autores";

        db.query(sql, [], (err, result) => {
            if (err) {
                res.writeHead(404, { "Content-Type": "text/plain" });
                res.end("Imagem não encontrada.");
                return;
            }
            // console.log(result);
            res.writeHead(200, { "Content-Type": result });
            res.end(JSON.stringify(result));
        });
    } else {
        res.writeHead(405, { "Content-Type": "text/plain" });
        res.end("Método não permitido.");
    }
});

// Iniciando o servidor na porta 3000
const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
});
