#!/usr/bin/node

if (!process.argv.slice(2)[0]) {
  console.log('No argument');
}
if (process.argv.slice(2)[0]) {
  console.log(process.argv.slice(2)[0]);
}
