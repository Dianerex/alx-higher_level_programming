const numArgs = process.argv.length - 2;

if (numArgs <= 1) {
  console.log(0);
} else {
  const integers = process.argv.slice(2).map(arg => parseInt(arg, 10));
  integers.sort((a, b) => b - a);

  console.log(integers[1]);
}
