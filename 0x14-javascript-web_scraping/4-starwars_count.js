#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];
request(URL, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const file = JSON.parse(body).results;
  let cnt = 0;
  for (const items in file) {
    for (const str in file[items].characters) {
      if (file[items].characters[str].includes('18')) {
        cnt += 1;
      }
    }
  }
  console.log(cnt);
});
