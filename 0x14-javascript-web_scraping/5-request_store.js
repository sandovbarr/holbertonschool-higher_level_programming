#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const urlRq = process.argv[2];
const fileToSave = process.argv[3];

request(urlRq).pipe(fs.createWriteStream(fileToSave));
