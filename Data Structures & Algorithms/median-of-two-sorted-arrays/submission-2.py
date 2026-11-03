class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        do binary search on smaller array
        that becomes a_i
        calculate b_i based off that

        partition index

        correct partition when a_left <= b_right and b_left <= a_right

        if a too big -> a taking up too might -> go left
        -> otherwise -> go right
        '''
        a, b = nums1, nums2
        total_size = len(a) + len(b)
        half_size = total_size // 2

        # ensure we do binary search on smaller item
        if len(b) < len(a):
            a, b = b, a

        # setup binary search on smaller list -> a
        l, r = 0, len(a) - 1

        while True:
            a_i = (l + r) // 2
            b_i = half_size - a_i - 2 # todo: why -2

            # calculate border values
            # todo: why left is i and right is i + 1
            a_left = a[a_i] if a_i >= 0 else float("-inf")
            a_right = a[a_i + 1] if (a_i + 1) < len(a) else float("inf")

            b_left = b[b_i] if b_i >= 0 else float("-inf")
            b_right = b[b_i + 1] if (b_i + 1) < len(b) else float("inf")

            valid_partition = a_left <= b_right and b_left <= a_right
            if valid_partition:
                # odd case
                if total_size % 2 == 1:
                    return min(a_right, b_right)
                # even case
                return (min(a_right, b_right) + max(a_left, b_left)) / 2
            
            if a_left > b_right:
                # a too big -> go left
                r = a_i - 1
            else:
                # a too small -> go right
                l = a_i + 1


        