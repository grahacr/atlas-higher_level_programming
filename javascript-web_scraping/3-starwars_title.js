#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const endPoint = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request.get(endPoint, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movieData = JSON.parse(body);
  console.log(movieData.title);
});
