from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:

    print(nums1, nums2)

    l1, l2 = len(nums1), len(nums2)
    if l1 > l2:
        l1, l2 = l2, l1
        nums1, nums2 = nums2, nums1
    left, right = 0, l1

    haft = (l1 + l2 + 1) // 2
    while 1:
        # i 代表 隔板位置
        i = (left + right) // 2
        j = haft - i

        #         print(i, j)
        if i > 0 and nums1[i - 1] > nums2[j]:
            #             print(nums1[i-1], nums2[j + 1])
            right = i - 1
        elif i < l1 and nums1[i] < nums2[j - 1]:
            #             print(nums1[i], nums2[j - 1])
            left = i + 1
        else:
            #             print(i, j)
            if i == 0:
                left_max = nums2[j - 1]
            elif j == 0:
                left_max = nums1[i - 1]
            else:
                left_max = max(nums1[i - 1], nums2[j - 1])

            if (l1 + l2) % 2 == 1:
                return left_max

            if i == l1:
                right_min = nums2[j]
            elif j == l2:
                right_min = nums1[i]
            else:
                right_min = min(nums1[i], nums2[j])

            return (left_max + right_min) / 2


if __name__ == "__main__":
    print(findMedianSortedArrays([1, 3], [2]))
    print(findMedianSortedArrays([1, 2], [3, 4]))

    print(findMedianSortedArrays([], [1]))
    print(findMedianSortedArrays([], [2, 3]))

    print(findMedianSortedArrays([1], []))
    print(findMedianSortedArrays([2, 3], []))

    print(findMedianSortedArrays([3], [-2, -1]))
