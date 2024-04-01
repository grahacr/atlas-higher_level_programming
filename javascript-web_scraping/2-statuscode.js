#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (response, body) => {
  if (response) {
    console.log('code:', response.statusCode);
  }
});
