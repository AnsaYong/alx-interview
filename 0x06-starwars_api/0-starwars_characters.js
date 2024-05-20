#!/usr/bin/node
console.log('Hi Ansa!')
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/film/3/';
request(url, function (error, response, body) {
  if (error) {
    console.error('Error making request:', error);
    return;
  }

  console.log('Status Code:', response && response.statusCode);
  console.log('Body:', body);
});