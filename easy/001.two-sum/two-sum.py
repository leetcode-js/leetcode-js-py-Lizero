class Solution:
    def twoSum(self, nums, target):
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if num1 + num2 == target:
                    return [i, i+j+1]


if __name__ == '__main__':
    s = Solution()
    twoSum = s.twoSum

    print(twoSum([2, 7, 11, 15], 9) == [0, 1])
