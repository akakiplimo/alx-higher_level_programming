#!/usr/bin/node
const lenArgs = process.argv.length - 2;
if (lenArgs === 0) {
  console.log('No argument');
} else if (lenArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
