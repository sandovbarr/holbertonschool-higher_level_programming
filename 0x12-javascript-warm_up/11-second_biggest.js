#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const size = process.argv.length;
  process.argv.sort();
  console.log(process.argv[size - 2]);
}
