class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        [left sorted, right sorted]

        1. find in which section
        if l < m, in left sorted, else in right sorted
        
        2. if in left sorted, 
            search right if mid < target or target < left
            search left if left < target < mid

        3. if in right sorted,
            search left if target < mid or right < target
            search right if mid < target < right
        '''
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            is_in_left_sorted = nums[left] <= nums[mid]
            if is_in_left_sorted:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else: #l < target < mid
                    right = mid - 1
            else: # in right sorted
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
        
        