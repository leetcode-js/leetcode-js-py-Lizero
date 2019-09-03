/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  let hash = {}
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in hash) {
      hash[nums[i]] += 1
    }
    else {
      hash[nums[i]] = 1
    }
  }
  const keys = Object.keys(hash)
  const positive = keys.map(parseInt).filter(n => n > 0)
  const negative = keys.map(parseInt).filter(n => n < 0)
  console.log(keys.map(parseInt))
  // console.log(negative)
  if (positive.length === 0 || negative.length === 0 || nums.length < 3) {
    return []
  }
  if (hash[0] > 3) {
    ans = [[0, 0, 0]]
  }
  else {
    ans = []
  }
  for (let i = 0; i < negative.length; i++) {
    for (let j = 0; j < positive.length; j++) {
      const result = -(+negative[i] + (+positive[j]))
      if (result === negative[i] && hash[result] > 1) {
        ans.push([negative[i], negative[i], positive[j]])
      }
      else if (result === positive[j] && hash[result] > 1) {
        ans.push([negative[i], positive[j], positive[j]])
      }
      else if (result in hash && negative[i] < result < positive[j]) {
        ans.push([negative[i], result, positive[j]])
      }
    }
  }
  return ans
};

console.log(threeSum([-1, -2, -3, 4, 1, 3, 0, 3, -2, 1, -2, 2, -1, 1, -5, 4, -3]
))