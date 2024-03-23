#!/usr/bin/node

function intCheck() {
    const argument = parseInt(process.argv[2]);
    if (!isNaN(argument)) {
        console.log("My number: " + argument);
    } else {
        console.log("Not a number");
    }
}
intCheck()
