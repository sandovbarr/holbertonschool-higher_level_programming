#!/usr/bin/node
const request = require('request');
const reqUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/?format=json';

request(reqUrl, function (response, error, body) {
  const info = JSON.parse(body);
  console.log(info.title);
});
