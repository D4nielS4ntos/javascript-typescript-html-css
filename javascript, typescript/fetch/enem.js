fetch(`https://api.enem.dev/v1/exams/2020/questions?limit=1&offset=10`)
.then(response => response.json())
.then(dado => {
    console.log(dado)
})
