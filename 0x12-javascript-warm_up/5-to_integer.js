#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
console.log(num);
console.log(process.argv.length);
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
