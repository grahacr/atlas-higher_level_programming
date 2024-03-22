#!/usr/bin/node

function varArgs() {
    if (process.argv.length === 2) {
        console.log("No argument");
    } else if (process.argv.length === 1) {
        console.log("Argument found");
    } else {
        console.log("Arguments found");
    }
}
varArgs();