#!/usr/bin/node

const arg = process.argv[2];
const num = Number(arg);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else if (num > 0) {
  for (let i = 0; i < Number(arg); i++) {
    console.log('C is fun');
  }
}
