#!/usr/bin/node
const getDict = require('./101-data').dict;
const newKeys = Object.values(getDict);
const uniqKeys = [...new Set(newKeys)];
const returnDict = {};
let kValues = [];

for (let idx = 0; idx < uniqKeys.length; idx++) {
  for (const key in getDict) {
    if (getDict[key] === uniqKeys[idx]) {
      kValues.push(key);
    }
  }
  returnDict[uniqKeys[idx]] = kValues;
  kValues = [];
}

console.log(returnDict);
