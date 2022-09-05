#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
if (myNum === undefined) {
  console.log('Not a number');
} else if (isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNum}`);
}
