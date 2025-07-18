#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  let max = -Infinity;
  let second = -Infinity;

  for (let i = 0; i < args.length; i++) {
    const current = args[i];

    if (current > max) {
      second = max;
      max = current;
    } else if (current < max && current > second) {
      second = current;
    }
  }

  console.log(second);
}
