#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let iter = 0; iter < this.height; iter++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}
