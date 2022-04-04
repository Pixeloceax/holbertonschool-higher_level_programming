#!/usr/bin/node

if (process.argv.slice(2)[0]) {
  console.log('My number:', parseInt(process.argv.slice(2)[0]));
}
if (isNaN(process.argv.slice(2)[0])) {
  console.log('Not a number');
}
