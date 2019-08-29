import re


class Solution:
    def myAtoi(self, str: str) -> int:
        return min(max(int(*re.findall(r'^[\-\+]?\d+', str.lstrip())), -1 << 31), (1 << 31)-1)


if __name__ == '__main__':
    s = Solution()
    myAtoi = s.myAtoi

    print(myAtoi('42') == 42)
    print(myAtoi("   -42") == -42)
    print(myAtoi("4193 with words") == 4193)
    print(myAtoi("words and 987") == 0)
    print(myAtoi("-91283472332") == -2147483648)
    print(myAtoi("      -11919730356x") == -2147483648)
