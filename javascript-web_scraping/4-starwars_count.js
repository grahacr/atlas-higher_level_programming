#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const findId = '18';

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  let count = 0;
  data.results.forEach(film => {
    if (film.characters) {
      film.characters.forEach(character => {
        const characterId = character.split('/');
        if (characterId === findId) {
          count++;
        }
      })
    }
  });
  console.log(count);
});
