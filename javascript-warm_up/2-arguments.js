#!/usr/bin/node

console.log(process.argv);
const args = process.argv.length;

if (args === 2) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
