#!/usr/bin/node

exports.nb0ccurences = function (list, searchElement) {
    let count = 0;
    for (let i = 0; i < list.length; i++) {
        if (list[i] === searchElement) {
            count++;
        }
    }
    return count;
}
module.exports = nb0ccurences;