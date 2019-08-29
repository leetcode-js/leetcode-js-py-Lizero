/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
// memo 自底而上
var isMatch = function (s, p) {
  let memo = { [`${s.length},${p.length}`]: true }
  for (let i = 0; i < s.length; i++) {
    memo[`${i},${p.length}`] = false
  }
  for (let i = s.length; i > -1; i--) {
    for (let j = p.length - 1; j > -1; j--) {
      firstMatch = i < s.length && (p[j] === '.' || p[j] === s[i])
      if (j + 1 < p.length && p[j + 1] === '*') {
        memo[`${i},${j}`] = memo[`${i},${j + 2}`] || firstMatch && memo[`${i + 1},${j}`]
      }
      else if (firstMatch) {
        memo[`${i},${j}`] = memo[`${i + 1},${j + 1}`]
      }
      else {
        memo[`${i},${j}`] = false
      }
    }
  }
  return memo['0,0']
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