#!/usr/bin/node

if (process.argv.slice(2)[0]) {
  console.log(process.argv.slice(2)[0], 'is', process.argv.slice(2)[1]);
} else if (process.argv.slice(2)[0]) {
  console.log(process.argv.slice(2)[0], 'is');
} else {
  console.log(process.argv.slice(2)[0], 'is', process.argv.slice(2)[1]);
}
