#!/usr/bin/node
const firstArgument = process.argv[2];
const integerValue = +firstArgument;
if (!isNaN(integerValue)) {
  console.log(`My number: ${integerValue}`);
} else {
  console.log('Not a number');
}
