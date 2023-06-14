#!/usr/bin/node
const args = process.argv.slice(2);
let string = '';
const n = Number(args[0]);
if (isNaN(args[0])) {
  console.log('Missing size');
}
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    string += 'X';
  }
  string += '\n';
}
console.log(string);
