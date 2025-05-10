const mysql = require('mysql');
// import { chomusuke } from './imagens';

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  database: 'ex_guardar_arquivo'
});

connection.connect((err) => {
  if (err) throw err;
  console.log('Connected!');

//   connection.query('SELECT * FROM imagens_blob', (err, result) => {
//     if (err) throw err;
//     console.log(result);
//   });

connection.query('INSERT INTO imagens_blob VALUES (?, ?)', ['chomusuke', ''], (err, result) => {
    if (err) throw err;
    console.log(result);
  });
});
