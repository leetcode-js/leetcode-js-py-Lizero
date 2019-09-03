class Solution:
    def intToRoman(self, num: int) -> str:
        ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC',
                  'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        ans, i = '', 0
        while num and i < 13:
            if num >= ints[i]:
                ans += romans[i]
                num -= ints[i]
            else:
                i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    intToRoman = s.intToRoman

    print(intToRoman(3) == 'III')
    print(intToRoman(4) == 'IV')
    print(intToRoman(9) == 'IX')
    print(intToRoman(58) == 'LVIII')
    print(intToRoman(1994) == 'MCMXCIV')
