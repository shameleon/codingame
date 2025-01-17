function getMin(a, b) {
    return a < b ? a : b;
  }

const L = parseInt(readline());
const N = parseInt(readline());
var inputs = readline().split(' ');
var left = L;
var right = 0;
for (let i = 0; i < N; i++) {
    const b = parseInt(inputs[i]);
    if (b < left) {left = b}
    if (b > right) {right = b}
}
var time = L - getMin(left, L - right)
//console.error('Debug messages...');
console.log(time);