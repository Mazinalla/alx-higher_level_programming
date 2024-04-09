#!/usr/bin/node
const numOccurrences = process.argv[2];
const integerValue = +numOccurrences;
if (!isNaN(integerValue)) {
  for (let i = 0; i < integerValue; i++) {
      console.log('C is fun');
    }
} else {
  console.log('Missing number of occurrences');
}
