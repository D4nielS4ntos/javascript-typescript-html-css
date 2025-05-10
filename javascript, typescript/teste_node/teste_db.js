const mysql = require('mysql');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  database: 'ex_biblioteca'
});

connection.connect((err) => {
  if (err) throw err;
  console.log('Connected!');
  connection.query('SELECT * FROM autores', (err, result) => {
    if (err) throw err;
    console.log(result);
  });
});
