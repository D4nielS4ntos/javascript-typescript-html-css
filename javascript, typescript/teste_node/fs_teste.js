const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
    // READ FILE
    // fs.readFile('./texto/kira_copypasta.txt', (err, data) => {
    //     res.writeHead(200, {'Content-Type': 'text/html'});
    //     res.write(data);
    //     res.end();
    // });
    // CREATE FILE
    // Appends specified content to a file. If the file does not exist, the file will be created
    // fs.appendFile('./texto/ola.txt', 'olá mundo\n', (err) => {
    //     if (err) throw err;
    //     console.log('Alteração salva com sucesso!');
    //     res.end('Alteração salva com sucesso!');
    // });
    // OPEN FILE
    // opens for writing and if the file does not exist, it is created
    // fs.open('./texto/file.txt', 'w', (err, file) => {
    //     if (err) throw err;
    //     console.log('Saved!');
    //     res.end('Saved!');
    // });
    // REWRITE FILE
    // replaces the content if it exists. If it does not exist, a new file with the content, will be created
    // fs.writeFile('./texto/novoArquivo.txt', 'Novo conteúdo!', (err) => {
    //     if (err) throw err;
    //     console.log('Arquivo salvo com sucesso!');
    //     res.end('Arquivo salvo com sucesso');
    // });
    // fs.appendFile('./texto/novoArquivo.txt', '\natualização do conteúdo!', (err) => {
    //     if (err) throw err;
    //     console.log('Arquivo salvo com sucesso!');
    //     res.end('Arquivo salvo com sucesso');
    // });
    // DELETE FILE
    // fs.unlink('./texto/deletado.txt', (err) => {
    //     if (err) throw err;
    //     console.log('Arquivo deletado com sucesso!');
    //     res.end('Arquivo deletado com sucesso');
    // });
    // RENAME FILE
    // renomear um arquivo ou mover para outro diretório são a mesma coisa na visão da máquina
    // fs.rename('./renomeado.txt', './texto/renomeado.txt', (err) => {
    //     if (err) throw err;
    //     console.log('Arquivo renomeado com sucesso!');
    //     res.end('Arquivo renomeado com sucesso');
    // });
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
});
