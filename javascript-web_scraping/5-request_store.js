#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const newFile = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(newFile, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
