#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length;
  for (let i = 0, j = len - 1; (len - i) > 0; i++, j--) {
    const tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
    len--;
  }
  return (list);
};
