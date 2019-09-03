class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        if num >= 1000:
            ans += 'M' * (num // 1000)
            num %= 1000
        if num >= 900:
            ans += 'CM'
            num -= 900
        if num >= 500:
            ans += 'D'
            num -= 500
        if num >= 400:
            ans += 'CD'
            num -= 400
        if num >= 100:
            ans += 'C' * (num // 100)
            num %= 100
        if num >= 90:
            ans += 'XC'
            num -= 90
        if num >= 50:
            ans += 'L'
            num -= 50
        if num >= 40:
            ans += 'XL'
            num -= 40
        if num >= 10:
            ans += 'X' * (num // 10)
            num %= 10
        if num == 9:
            ans += 'IX'
            num = 0
        if num >= 5:
            ans += 'V'
            num -= 5
        if num == 4:
            ans += 'IV'
            num = 0
        if num > 0:
            ans += 'I' * num
        return ans


if __name__ == '__main__':
    s = Solution()
    intToRoman = s.intToRoman

    print(intToRoman(3) == 'III')
    print(intToRoman(4) == 'IV')
    print(intToRoman(9) == 'IX')
    print(intToRoman(58) == 'LVIII')
    print(intToRoman(1994) == 'MCMXCIV')
