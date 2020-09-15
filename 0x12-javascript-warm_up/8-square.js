#!/usr/bin/node
if (parseInt(process.argv[2])) {
  for (let iter = 0; iter < parseInt(process.argv[2]); iter++) {
    console.log('X'.repeat(process.argv[2]));
  }
} else {
  console.log('Missing size');
}
