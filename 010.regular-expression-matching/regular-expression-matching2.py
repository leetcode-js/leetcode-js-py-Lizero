# 解法2：根据第二个位置情况分类
class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not bool(s)
        if not s:
            return len(p) % 2 == 0 and all([i == '*' for i in p[1::2]])

        firstMatch = p[0] == s[0] or p[0] == '.'

        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or firstMatch and self.isMatch(s[1:], p)
        if firstMatch:
            return self.isMatch(s[1:], p[1:])
        return False


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
