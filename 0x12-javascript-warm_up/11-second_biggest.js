#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = process.argv.slice(2);
  arr.sort(function (a, b) { return a - b; });
  console.log(arr[arr.length - 2]);
}
