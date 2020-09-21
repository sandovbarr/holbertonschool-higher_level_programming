#!/usr/bin/node
const getList = require('./100-data').list;
const mapList = getList.map((x, index) => x * index);
console.log(getList);
console.log(mapList);
