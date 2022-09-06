#!/usr/bin/node
const Rectangle = require('./4-rectangle');

// inheriting parent class
class Square extends Rectangle {
  // call the super class constructor and pass the size parameter as width & height
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
