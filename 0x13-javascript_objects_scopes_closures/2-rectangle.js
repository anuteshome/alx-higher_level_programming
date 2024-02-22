#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w === 0 || h === 0) || (w < 0 || h < 0) || (w === undefined || h === undefined)) {
      Rectangle[''] = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
