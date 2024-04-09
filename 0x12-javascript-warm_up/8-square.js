#!/usr/bin/node
const size = process.argv[2];
const intValue = +size;
if (!isNaN(intValue)) {
  for (let i = 0; i < intValue; i++) {
    let row = '';
    for (let j = 0; j < intValue; j++) {
      row += 'X';
    }
    console.log(row);
  }
  } else {
  console.log("Missing size");
  }
