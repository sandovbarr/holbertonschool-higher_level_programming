#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let times = 0;
  for (let iter = 0; iter < list.length; iter++) {
    if (list[iter] === searchElement) {
      times++;
    }
  }
  return times;
};
