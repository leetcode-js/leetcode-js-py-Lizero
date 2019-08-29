# 解法3：带memo 自底而上
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        sLen = len(s)
        pLen = len(p)
        memo = {(sLen, pLen): True}
        for i in range(sLen):
            memo[i, pLen] = False

        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                firstMatch = i < len(s) and (p[j] == '.' or s[i] == p[j])
                if j + 1 < len(p) and p[j + 1] == '*':
                    memo[i, j] = memo[i, j+2] or firstMatch and memo[i+1, j]
                elif firstMatch:
                    memo[i, j] = memo[i + 1, j + 1]
                else:
                    memo[i, j] = False
        return memo[0, 0]


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
