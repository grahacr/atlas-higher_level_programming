#!/usr/bin/node

const number = parseInt(process.argv[2]);

function factorialRecursive (number) {
  if (isNaN(number) || number < 0 || number === 0) {
    return 1;
  }
  return number * factorialRecursive(number - 1);
}
console.log(factorialRecursive(number));
