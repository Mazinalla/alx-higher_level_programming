#!/usr/bin/node
const firstarg = process.argv[2];
if (firstarg === undefined) {
  console.log('No argument');
} else {
  console.log(firstarg);
}
