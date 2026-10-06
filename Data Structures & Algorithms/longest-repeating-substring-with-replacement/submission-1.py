class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''

        window, keep track of number of differences
        
        have freq map
        differences is window size - count most freq char

        if differences > k, shift window
            shift left pointer until differences = k

        shift right pointer

        keep track of largest window size
              
        '''

        '''
        - difference <= k
        - difference: window size - count of most common char -> window size - largest item in freq map
        - if violate rule -> shrink window -> shift l
        - when to shift r
        '''
        char_to_freq = defaultdict(int)
        best_window_size = 0
        window_size = 0

        l = 0

        for r in range(len(s)):
            char = s[r]
            char_to_freq[char] += 1
            window_size += 1

            most_common_char_count = max(char_to_freq.values())
            difference = window_size - most_common_char_count

            if difference > k:
                deleted_char = s[l]
                char_to_freq[deleted_char] -= 1
                l += 1
                window_size -= 1
            
            best_window_size = max(window_size, best_window_size)

        return best_window_size
        