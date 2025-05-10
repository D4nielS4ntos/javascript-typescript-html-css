// const http = require('http');
// const fs = require('fs');
// const formidable = require('formidable');

// const server = http.createServer(function (req, res) {
//   if (req.url == '/fileupload' && req.method.toLowerCase() === 'post') {
//     const form = new formidable.IncomingForm();
//     form.parse(req, (err, fields, files) => {
//         if (err) {
//             res.writeHead(500, {'Content-Type': 'text/plain'});
//             res.write('Error parsing the file');
//             return res.end();
//         }
//         const oldpath = files.filetoupload.filepath;
//         const newpath = 'C:\\Users\\Danie\\OneDrive\\Área de Trabalho\\Programação\\Exercícios\\javascript, typescript\\teste_node\\texto\\' + files.filetoupload.originalFilename;
//         fs.rename(oldpath, newpath, (err) => {
//             if (err) {
//                 res.writeHead(500, {'Content-Type': 'text/plain'});
//                 res.write('Error moving the file');
//                 return res.end();
//             }
//             res.writeHead(200, {'Content-Type': 'text/plain'});
//             res.write('File uploaded and moved!');
//             return res.end();
//         });
//     });
//   } else {
//     fs.readFile('./texto/upArquivos.html', (err, data) => {
//         if (err) {
//             res.writeHead(500, {'Content-Type': 'text/plain'});
//             res.write('Error loading the form');
//             return res.end();
//         }
//         res.writeHead(200, {'Content-Type': 'text/html'});
//         res.write(data);
//         return res.end();
//     });
//   }
// });

// server.listen(3000, () => {
//     console.log('Server is running on http://localhost:3000');
// });