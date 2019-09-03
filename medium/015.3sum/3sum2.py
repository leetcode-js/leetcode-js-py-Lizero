from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        positive = [i for i in set(nums) if i > 0]
        negative = [i for i in set(nums) if i < 0]
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        if 0 in hash and hash[0] > 2:
            ans = [[0, 0, 0]]
        else:
            ans = []
        if not (positive and negative) or len(nums) < 3:
            return ans
        for j in negative:
            for i in positive:
                result = -(i + j)
                if result == i and hash[i] > 1:
                    ans.append([j, i, i])
                elif result == j and hash[j] > 1:
                    ans.append([j, j, i])
                elif result in hash and j < result < i:
                    ans.append([j, result, i])
        return ans


if __name__ == "__main__":
    s = Solution()
    threeSum = s.threeSum

    print(threeSum([-1, 0, 1, 2, -1, -4]))
    print(threeSum([0, 0, 0, 0]) == [[0, 0, 0]])
    print(threeSum([]) == [])
    print(threeSum([1, -1]) == [])
    print(threeSum([1, 2, -2, -1]) == [])
    print(threeSum([1, 1, -2]) == [[-2, 1, 1]])
    print(len(threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])))
    print(
        threeSum([-1, -2, -3, 4, 1, 3, 0, 3, -2, 1, -2, 2, -1, 1, -5, 4, -3]))
