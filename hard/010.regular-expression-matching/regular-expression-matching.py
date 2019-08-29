# 解法1：根据第一个位置情况分类
class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        if not (bool(s) | bool(p)):
            return True
        if s and not p:
            return False
        if not s and p:
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:])
            return False

        if p[0] == s[0]:
            if len(p) > 1 and p[1] == '*':
                if len(p) > 2:
                    i = 0
                    l = len(s)
                    while i < l:
                        if self.isMatch(s[i:], p[2:]):
                            return True
                        if s[i] != p[0]:
                            return False
                        i += 1
                    if len(p) % 2 == 1 or not all(map(lambda x: x == '*', p[1::2])):
                        return False
                for i in s:
                    if i != p[0]:
                        return False
                return True
            return self.isMatch(s[1:], p[1:])

        if p[0] == '.':
            if len(p) > 1 and p[1] == '*':
                if len(p) > 2:
                    i = 0
                    l = len(s)
                    while i < l:
                        if self.isMatch(s[i:], p[2:]):
                            return True
                        i += 1
                    if len(p) % 2 == 0 and all(map(lambda x: x == '*', p[1::2])):
                        return True
                    return False
                return True
            return self.isMatch(s[1:], p[1:])

        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:])
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
