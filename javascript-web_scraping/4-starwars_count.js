#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const findId = '18/';
const charUrl = 'https://swapi-api.hbtn.io/api/people/';

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body).results;
  let count = 0;
  data.forEach(film => {
    const characters = film.characters;
    if (characters.include(charUrl + findId)) {
      count++;
    }
  });
  console.log(count);
});
