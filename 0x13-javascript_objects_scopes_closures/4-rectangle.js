#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h){
    // if w & h are positive integers create Rectangle otherwise create empty Rectangle
    if (w > 0 && h > 0)
    {
      this.width = w;
      this.height = h;
    }
  }

  print(){
    for (let i = 0; i < this.height; i++){
      for (let j = 0; j < this.width; j++){
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }

  rotate(){
    let length = this.width + this.height;
    this.width = length - this.width;
    this.height = length - this.height;
  }

  double(){
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
