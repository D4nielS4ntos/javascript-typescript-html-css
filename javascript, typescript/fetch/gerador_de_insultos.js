const myHeaders = new Headers();
myHeaders.append("Accept", "application/json");


const requestOptions = {
  method: "GET",
  headers: myHeaders,
  redirect: "follow"
};


fetch("https://evilinsult.com/generate_insult.php?lang=pt&type=json", requestOptions)
  .then((response) => response.text())
  .then((response) => JSON.parse(response))
  .then((result) => console.log(result.insult))
  .catch((error) => console.error(error))
