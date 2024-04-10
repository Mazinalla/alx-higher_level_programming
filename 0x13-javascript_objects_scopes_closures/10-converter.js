#!/usr/bin/node
exports.converter = function (base) {
  function convertRecursive (number) {
    const digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if (number < base) {
      return digits[number];
    }
    return convertRecursive(Math.floor(number / base)) + digits[number % base];
  }
  return convertRecursive;
};
