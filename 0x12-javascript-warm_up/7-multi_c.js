#!/usr/bin/node
if (parseInt(process.argv[2])) {
  for (let iter = 0; iter < parseInt(process.argv[2]); iter++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
