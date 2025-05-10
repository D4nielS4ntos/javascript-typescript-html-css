const express = require('express');
const path = require('path')
const app = express();
const port = 3000;

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, '/index.html'));
    }
)


// Rota para fornecer dados JSON
app.get('/api/mensagem', (req, res) => {
  const mensagem = {
    mensagem: 'Olá do Express!'
  };
  res.send(mensagem);
});

// Iniciar o servidor
app.listen(port, () => {
  console.log(`Servidor ouvindo na porta ${port}`);
});
