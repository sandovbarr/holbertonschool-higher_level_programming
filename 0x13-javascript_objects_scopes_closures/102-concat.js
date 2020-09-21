#!/usr/bin/node
const fs = require('fs');
const firstFile = process.argv[2];
const secondFile = process.argv[3];
const destination = process.argv[4];
const files = [firstFile, secondFile];
const stream = fs.createWriteStream(destination);

for (const el in files) {
  stream.once('open', function (fd) {
    fs.readFile(files[el], 'utf8', function (err, data) {
      if (err) {
        return console.log(err);
      }
      stream.write(data);
    });
  });
}
