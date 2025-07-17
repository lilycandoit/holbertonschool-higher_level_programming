#!/usr/bin/node

const arg = process.argv[2];
const num = Number(arg);

if (isNaN(num)) {
  console.log('Missing size');
} else if (num > 0) {
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
