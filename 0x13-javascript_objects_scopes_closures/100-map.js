#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const map1 = list.map(function (number, index) {
  return number * index;
}
);
console.log(map1);
