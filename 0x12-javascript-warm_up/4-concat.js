#!/usr/bin/node
const firstArgument = process.argv[2];
const secondArgument = process.argv[3];

if (firstArgument !== undefined && secondArgument !== undefined) {
  console.log(`${firstArgument} is ${secondArgument}`);
} else {
  console.log("Please provide two arguments.");
}
