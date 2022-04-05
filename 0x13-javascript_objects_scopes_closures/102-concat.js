#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (fileA && fileB && fileC) {
  const fs = require('fs');
  let file = '';
  file += fs.readFileSync(fileA);
  file += fs.readFileSync(fileB);
  fs.writeFileSync(fileC, file);
}
