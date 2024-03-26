#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      this.isEmpty = true;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
