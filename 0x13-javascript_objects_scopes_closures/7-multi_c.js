#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0])) {
  console.log('Missing number of occurrences');
} else {
  const num = Number(args[0]) - 1;
  for (let i = 0; i <= num; i++) {
    console.log('C is fun');
  }
}
