const nodemailer = require('nodemailer');
const fs = require('fs');

const transporter = nodemailer.createTransport({
    host: 'smtp.gmail.com',
    port: 465,
    secure: true,
    auth: {
      user: 'daniel632.ds@gmail.com',
      pass: 'adhhjwjakbytbloc'
    }
});

fs.readFile('./texto/teste.html', (err, data) => {
    if (err) {
        console.log(err);
    }

    const dataHTML = data;
    const mailOptions = {
        from: 'daniel632.ds@gmail.com',
        to: ['daniel632.ds@gmail.com','andrade.d@escolar.ifrn.edu.br'],
        subject: 'Sending Email using Node.js',
        html: `${dataHTML}`
    };

    transporter.sendMail(mailOptions)
    .then(() => {
        console.log("Email enviado!");
    })
    .catch((err) => {
        console.log(err);
    });
});
