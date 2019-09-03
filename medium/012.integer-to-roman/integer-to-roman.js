/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
  const ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  const romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

  let ans = ''
  for (let i = 0; num && i < 13;) {
    if (num >= ints[i]) {
      ans += romans[i]
      num -= ints[i]
    }
    else {
      i++
    }
  }
  return ans
};

console.log(intToRoman(3) == 'III')
console.log(intToRoman(4) == 'IV')
console.log(intToRoman(9) == 'IX')
console.log(intToRoman(58) == 'LVIII')
console.log(intToRoman(1994) == 'MCMXCIV')