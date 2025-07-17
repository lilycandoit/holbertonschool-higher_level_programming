#!/usr/bin/node

const arg1 = Number(process.argv[2]);
const arg2 = Number(process.argv[3]);

if (arg1 === undefined || arg2 === undefined || isNaN(arg1) || isNaN(arg2)) {
  console.log('NaN');
} else {
  console.log(add(arg1, arg2));
}

function add (a, b) {
  return a + b;
}
