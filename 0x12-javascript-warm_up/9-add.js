#!/usr/bin/node
function add (a, b) {
  return a + b;
}

if (parseInt(process.argv[2]) && parseInt(process.argv[3])) {
  console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
} else {
  console.log(NaN);
}
