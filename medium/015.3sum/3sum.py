from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        if not nums or nums[len(nums) - 1] < 0:
            return []
        for i in range(0, len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k and nums[k] >= 0:
                result = nums[i] + nums[j] + nums[k]
                if result == 0 and [nums[i], nums[j], nums[k]] not in ans:
                    ans.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    while j < k-1 and nums[k] == nums[k+1]:
                        k -= 1
                    j += 1
                    while j + 1 < k and nums[j - 1] == nums[j]:
                        j += 1
                elif result > 0:
                    k -= 1
                    while j < k-1 and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    j += 1
                    while j + 1 < k and nums[j - 1] == nums[j]:
                        j += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    threeSum = s.threeSum

    print(threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
    print(threeSum([0, 0, 0, 0]) == [[0, 0, 0]])
    print(threeSum([]) == [])
