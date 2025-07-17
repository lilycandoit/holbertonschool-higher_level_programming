#!/usr/bin/node

const arg = process.argv[2]; // first arg

// check if arg can be converted into number
if (isNaN(Number(arg))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(arg));
}
