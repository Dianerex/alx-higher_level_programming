#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arg = parseInt(process.argv)
  const list = arg.sort();
  console.log(list.reverse()[1]);
}
