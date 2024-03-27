#!/usr/bin/node

exports.esrever = function (list) {
  const reverseArray = [];
  for (i = list.length - 1; i >= 0; i--) {
    reverseArray.push(list[i]);
  }
  return reverseArray;
};
