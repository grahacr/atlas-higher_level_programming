#!/usr/bin/node

exports.logMe = function (item) {
    for (let i = 0; i < item.length; i++) {
        let string = `${i}: ${item}`;
        console.log(string);
    }
}