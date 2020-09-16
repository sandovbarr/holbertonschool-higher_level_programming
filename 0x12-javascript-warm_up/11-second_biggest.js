#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  process.argv = process.argv.slice(2,)
  process.argv.sort(((a, b) => a - b));
  console.log(process.argv[2])
}
