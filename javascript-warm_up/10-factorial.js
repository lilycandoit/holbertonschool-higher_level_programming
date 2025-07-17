#!/usr/bin/node

// Write a script that computes and prints a factorial

const arg = Number(process.argv[2]);

function factorial (n) {
  if (n <= 1 || isNaN(n)) return 1;
  return n * factorial(n - 1);
}

console.log(factorial(arg));
