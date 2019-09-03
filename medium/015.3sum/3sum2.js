/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  if (nums.length < 3) {
    return []
  }
  nums.sort((a, b) => a - b)
  console.log(nums)
  ans = []
  for (let f = 0; f < nums.length - 2;) {
    if (nums[f] > 0) {
      break
    }
    s = f + 1
    t = nums.length - 1
    while (s < t) {
      result = nums[f] + nums[s] + nums[t]
      console.log(result)
      if (result === 0) {
        ans.push([nums[f], nums[s], nums[t]])
        s++
        while (nums[s] === nums[s - 1] && s < t) {
          s++
        }
        t--
        while (nums[t] === nums[t + 1] && s < t) {
          t--
        }
      }
      else if (result > 0) {
        t--
        while (nums[t] === nums[t + 1] && s < t) {
          t--
        }
      }
      else {
        s++
        while (nums[s] === nums[s - 1] && s < t) {
          s++
        }
      }
      console.log(ans)
    }
    f++
    while (nums[f - 1] === nums[f]) {
      f++
    }
  }
  return ans
};

// console.log(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
// console.log(threeSum([0, 0, 0, 0]) , [[0, 0, 0]])
// console.log(threeSum([]) , [])
console.log(threeSum(
  [-1, -2, -3, 4, 1, 3, 0, 3, -2, 1, -2, 2, -1, 1, -5, 4, -3]), [[-5, 1, 4], [-5, 2, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -2, 4], [-2, -1, 3], [-2, 0, 2], [-2, 1, 1], [-1, -1, 2], [-1, 0, 1]])
