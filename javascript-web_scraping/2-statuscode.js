#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    if (response) {
        console.log('code:', response.statusCode);
  }
});
