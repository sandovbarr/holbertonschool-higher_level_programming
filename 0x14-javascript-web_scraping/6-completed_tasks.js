#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];
request(URL, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const file = JSON.parse(body);
  const listIds = [];
  let tasksCompleted = [];
  const objReturn = {};

  for (let iter = 0; iter < file.length; iter++) {
    if (!listIds.includes(file[iter].userId)) {
      listIds.push(file[iter].userId);
    }
  }

  for (const id in listIds) {
    for (let iter = 0; iter < file.length; iter++) {
      if (file[iter].userId === listIds[id]) {
        if (file[iter].completed === true) {
          tasksCompleted.push(1);
        }
      }
    }
    objReturn[listIds[id]] = tasksCompleted.length;
    tasksCompleted = [];
  }
  return console.log(objReturn);
});
