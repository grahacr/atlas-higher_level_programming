#!/usr/bin/node

const integers = process.argv.slice(2).map(arg => parseInt(arg))

integers.sort((a, b) => b - a);

let secondBiggest;
if (integers.length === 2 || integers.length === 3) {
    return 0
} else {
    secondBiggest = integers[1];
}
console.log(secondBiggest)