#!/usr/bin/node
exports.esrever = function (list) {
  const returnlist = [];
  for (let i = 0; i < list.length; i++) {
    returnlist.unshift(list[i]);
  }
  return returnlist;
};
