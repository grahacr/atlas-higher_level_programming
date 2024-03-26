#!/usr/bin/node

const integers = process.argv.slice(2).map(arg => parseInt(arg));

integers.sort((a, b) => b - a);

let secondBiggest;
if (integers.length === 0) {
  secondBiggest = 0;
} else if (integers.length === 1) {
  secondBiggest = integers[0];
} else {
  secondBiggest = integers[1];
}
console.log(secondBiggest);
