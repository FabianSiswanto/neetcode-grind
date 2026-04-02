class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        - two pointers -> one left, one right
        - if between left and right -> move pointer with lower height
            -> as bottleneck is lower height -> moving that will cause next area >= cur area

        area: width * height
            - width = r - l
            - height = min(left height, right height) -> bottleneck is lower height
        '''
        l = 0
        r = len(heights) - 1
        res = 0

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            area = w * h

            res = max(area, res)

            if heights[l] >= heights[r]: #right is shorter
                r -= 1
            else:
                l += 1

        return res