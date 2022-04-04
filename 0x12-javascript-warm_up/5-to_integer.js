#!/usr/bin/node

if (isNaN(parseInt(process.argv.slice(2)[0]))) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv.slice(2)[0]));
}
