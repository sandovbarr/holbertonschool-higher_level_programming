#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
