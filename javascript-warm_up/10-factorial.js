#!/usr/bin/node

const number = parseInt(process.argv[2]);

function factorialRecursive(number) {
    if (number === 0 || number === 1) {
        return 1;
    }
    return number * factorialRecursive(number - 1);
}
console.log(factorialRecursive(number))
