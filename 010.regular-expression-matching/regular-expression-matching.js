/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
// memo 自顶而下
var isMatch = function (s, p) {
  let memo = {}
  const match = (i, j) => {
    if (`${i},${j}` in memo) {
      return memo[`${i},${j}`]
    }
    if (j === p.length) {
      return i === s.length
    }
    const firstMatch = i < s.length && (p[j] == '.' || p[j] == s[i])
    if (j + 1 < p.length && p[j + 1] == '*') {
      memo[`${i},${j}`] = match(i, j + 2) || firstMatch && match(i + 1, j)
      return memo[`${i},${j}`]
    }
    if (firstMatch) {
      memo[`${i},${j}`] = match(i + 1, j + 1)
      return memo[`${i},${j}`]
    }
    memo[`${i},${j}`] = false
    return memo[`${i},${j}`]
  }
  return match(0, 0)
};

console.log(isMatch("aa", "a") == false)
console.log(isMatch("aa", "a*") == true)
console.log(isMatch("ab", ".*") == true)
console.log(isMatch("fghijkae", ".*ae") == true)
console.log(isMatch("aab", "c*a*b") == true)
console.log(isMatch("mississippi", "mis*is*p*.") == false)
console.log(isMatch("aaa", "a*a") == true)
console.log(isMatch("aaa", "ab*a*c*a") == true)
console.log(isMatch("abbabaaaaaaacaa", "a*.*b.a.*c*b*a*c*") == true)
console.log(isMatch("bcbabcaacacbcabac", "a*c*a*b*.*aa*c*a*a*") == true)