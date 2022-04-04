#!/usr/bin/node

let i = process.argv.slice(2)[0];

if (isNaN(parseInt(i))) {
  console.log('Missing number of occurrences');
} else if (i > 0) {
  while (i) {
    console.log('C is fun');
    i -= 1;
  }
}
