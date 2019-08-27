class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lenght = len(s)
        step = 2 * (numRows - 1)
        result = s[::step]
        for i in range(1, numRows - 1):
            index = i
            while index < lenght:
                result += s[index]
                index += step - i*2
                if index < lenght:
                    result += s[index]
                    index += i * 2
        result += (s[numRows-1::step])

        return result


if __name__ == '__main__':
    s = Solution()
    convert = s.convert

    print(convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
    print(convert(s="LEETCODEISHIRING", numRows=3) == "LCIRETOESIIGEDHN")
    print(convert(s="LEETCODEISHIRING", numRows=4) == "LDREOEIIECIHNTSG")
