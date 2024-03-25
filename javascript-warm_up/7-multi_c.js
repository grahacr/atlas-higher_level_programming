#!/usr/bin/node

function printC(x) {
  if (isNaN(parseInt(x, 10))) {
    console.log('Missing number of occurences');
  } else {
    for (let i = 0; i <= x; i++) {
      console.log('C is fun');
    }
  }
}
