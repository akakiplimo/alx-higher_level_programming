#!/usr/bin/node
const sourceA = process.argv[2];
const sourceB = process.argv[3];
const dest = process.argv[4];
const fs = require('fs');
const srcTextA = fs.readFileSync(sourceA);
const srcTextB = fs.readFileSync(sourceB);
fs.writeFileSync(dest, srcTextA + srcTextB);
