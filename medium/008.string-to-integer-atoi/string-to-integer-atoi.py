class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        r = 0
        sign = 1
        if not s:
            return 0
        if s[0] in ['+', '-']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        for i in s:
            try:
                j = int(i)
            except:
                break
            else:
                r = 10 * r + j

        r = r*sign
        if -1 << 31 <= r <= (1 << 31)-1:
            return r
        elif sign < 0:
            return - 1 << 31
        return (1 << 31) - 1


if __name__ == '__main__':
    s = Solution()
    myAtoi = s.myAtoi

    print(myAtoi('42') == 42)
    print(myAtoi("   -42") == -42)
    print(myAtoi("4193 with words") == 4193)
    print(myAtoi("words and 987") == 0)
    print(myAtoi("-91283472332") == -2147483648)
    print(myAtoi("      -11919730356x") == -2147483648)
