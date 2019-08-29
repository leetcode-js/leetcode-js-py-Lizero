# 解法3：带memo 自顶而下
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def match(i, j):
            if (i, j) in memo:
                return memo[i, j]

            if j == len(p):
                memo[i, j] = i == len(s)
                return memo[i, j]
            firstMatch = i < len(s) and (p[j] == '.' or p[j] == s[i])
            if j + 1 < len(p) and p[j + 1] == '*':
                memo[i, j] = match(i, j + 2) or firstMatch and match(i + 1, j)
                return memo[i, j]
            memo[i, j] = firstMatch and match(i + 1, j + 1)
            return memo[i, j]

        return match(0, 0)


if __name__ == '__main__':
    s = Solution()
    isMatch = s.isMatch

    print(isMatch("aa", "a") == False)
    print(isMatch("aa", "a*") == True)
    print(isMatch("ab", ".*") == True)
    print(isMatch("fghijkae", ".*ae") == True)
    print(isMatch("aab", "c*a*b") == True)
    print(isMatch("mississippi", "mis*is*p*.") == False)
    print(isMatch("aaa", "a*a") == True)
    print(isMatch("aaa", "ab*a*c*a") == True)
    print(isMatch("abbabaaaaaaacaa", "a*.*b.a.*c*b*a*c*") == True)
    print(isMatch("bcbabcaacacbcabac", "a*c*a*b*.*aa*c*a*a*") == True)
