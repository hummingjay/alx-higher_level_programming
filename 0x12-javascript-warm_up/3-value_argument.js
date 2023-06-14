#!/usr/bin/node
let n = process.argv.slice(2);
if (n[0]) {
  console.log(n[0]);
} else {
  console.log('No argument');
}
