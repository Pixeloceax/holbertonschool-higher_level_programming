#!/usr/bin/node

function factorial (n) {
  const index = 1;
  if (n > 1) {
    return n * factorial(n - 1);
  }
  return index;
}

console.log(factorial(Number(process.argv[2])));
