const nodemailer = require('nodemailer');
// const cron = require('node-cron');
const fs = require('fs');

const transporter = nodemailer.createTransport({
    host: 'smtp.gmail.com',
    port: 465,
    secure: true,
    auth: {
      user: 'contasuspeitadeumdesconhecido@gmail.com',
      pass: 'kxqk avfi mnbm aikr'
    }
});

fs.readFile('./email.html', (err, data) => {
    if (err) {
        console.log(err);
    }

    const dataHTML = data;
    const mailOptions = {
        from: 'contasuspeitadeumdesconhecido@gmail.com',
        to: ['daniel.santos.138@ufrn.edu.br', 'viannab403@gmail.com', 'reicoxinha0@gmail.com', 'felipe.bizerra@escolar.ifrn.edu.br', 'bezerrafelipe742@gmail.com', 'lopes.vitor@escolar.ifrn.edu.br', 'vitor036daniel@gmail.com'],
        /*
        viannab403@gmail.com
        reicoxinha0@gmail.com
        felipe.bizerra@escolar.ifrn.edu.br
        bezerrafelipe742@gmail.com
        lopes.vitor@escolar.ifrn.edu.br
        vitor036daniel@gmail.com
        */
        subject: 'Sending Email using Node.js',
        html: `${dataHTML}`
    };

    // cron.schedule("", () => {
    //     console.log("Executando tarefa agendada...");
    // }

    // );
    transporter.sendMail(mailOptions)
    .then(() => {
        console.log("Email enviado!");
    })
    .catch((err) => {
        console.log(err);
    });
});
