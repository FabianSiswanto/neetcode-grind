class Solution:
    def reverse(self, x: int) -> int:
        '''
        check negative first -> if yes convert to pos -> return -res in end

        right to left:
        -> right most digit: x % 10
        -> x = x / 10
        -> res = right most digit + 10 * res
        -> overflow check

        left to right:
            find div -> multiply while div * 10 < x

            digit = 1
            take left most digit -> res += left digit * 10^digit
            increment digit
            divide div by 10
        '''
        is_negative = x < 0
        if is_negative:
            x = -x

        res = 0

        while x:
            right_most = x % 10
            x = x // 10
            res = right_most + res * 10

            within_32int_range = -pow(2, 31) <= res <= pow(2, 31) - 1
            if not within_32int_range:
                return 0

        return res if not is_negative else -res
