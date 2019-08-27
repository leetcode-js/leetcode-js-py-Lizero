/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function (str) {
  const r = parseInt(str)
  return isNaN(r) ? 0 : r < 1 << -1 ? 1 << -1 : r > ~(1 << -1) ? ~(1 << -1) : r
};


console.log(myAtoi('42') === 42)
console.log(myAtoi("   -42") === -42)
console.log(myAtoi("4193 with words") === 4193)
console.log(myAtoi("words and 987") === 0)
console.log(myAtoi("-91283472332") === -2147483648)
console.log(myAtoi("      -11919730356x") === -2147483648)
