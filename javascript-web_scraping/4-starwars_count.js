#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  const findId = '18';
  let count = 0;
  data.forEach(item => {
    if (item.id === findId) {
      count++;
    }
  });
  console.log(count);
});
