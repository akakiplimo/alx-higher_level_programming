#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    // if w & h are positive integers create Rectangle otherwise create empty Rectangle
    if (w > 0 && h > 0)
    {
      this.width = w;
      this.height = h;
    }
  }
};
