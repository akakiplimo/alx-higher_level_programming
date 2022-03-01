#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const num in list) {
    if (list[num] === searchElement) {
      i++;
    }
  }
  return (i);
};
