#!/usr/bin/node

const n = process.argv.slice(2)[0];

if (isNaN(parseInt(n))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
