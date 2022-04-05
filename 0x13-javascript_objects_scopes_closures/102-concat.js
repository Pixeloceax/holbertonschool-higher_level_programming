#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const fs = require('fs');
const fileA_content = fs.readFileSync(fileA, 'utf8');
const fileB_content = fs.readFileSync(fileB, 'utf8');
const fileC_content = fs.readFileSync(fileC, 'utf8');
console.log(fileA_content + fileB_content + fileC_content);

