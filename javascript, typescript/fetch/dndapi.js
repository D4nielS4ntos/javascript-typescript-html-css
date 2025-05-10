const myHeaders = new Headers();
myHeaders.append("Accept", "application/json");


const requestOptions = {
  method: "GET",
  headers: myHeaders,
  redirect: "follow"
};


fetch("https://api.open5e.com/v1/spells/", requestOptions)
  .then((response) => response.text())
  .then((text) => JSON.parse(text))
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
