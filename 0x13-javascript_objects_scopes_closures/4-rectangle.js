#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w <= 0 || h <= 0) || (!w || !h)) {
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let iter = 0; iter < this.height; iter++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const swapper = this.width;
    this.width = this.height;
    this.height = swapper;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
