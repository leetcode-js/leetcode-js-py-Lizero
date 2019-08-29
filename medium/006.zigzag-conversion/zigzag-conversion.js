/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  const step = 2 * (numRows - 1)
  const len = s.length
  let result = ''

  for (let i = 0; i < len; i += step) {
    result += s[i]
  }

  for (let i = 1; i < numRows - 1; i += 1) {
    let index = i
    // console.log(len)
    while (index < len) {
      // console.log(s[index])
      result += s[index]
      index += step - 2 * i
      if (index < len) {
        result += s[index]
        index += 2 * i
      }
    }
  }

  for (let i = numRows - 1; i < len; i += step) {
    result += s[i]
  }

  return result
};

console.log(convert("PAYPALISHIRING", 3) === "PAHNAPLSIIGYIR")
console.log(convert(s = "LEETCODEISHIRING", numRows = 3) == "LCIRETOESIIGEDHN")
console.log(convert(s = "LEETCODEISHIRING", numRows = 4) == "LDREOEIIECIHNTSG")
