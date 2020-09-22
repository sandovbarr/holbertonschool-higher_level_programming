#!/usr/bin/node
const request = require('request');
const reqUrl = process.argv[2] + '/?format=json';
const character = 'https://swapi-api.hbtn.io/api/people/18/';

request(reqUrl, (response, error, body) => {
  const info = JSON.parse(body);
  const allMovies = info.results;
  let numberMovies = 0;

  for (let iter = 0; iter < allMovies.length; iter++) {
    if (allMovies[iter].characters.includes(character)) {
      numberMovies++;
    }
  }
  console.log(numberMovies);
});
