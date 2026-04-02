from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        - can build group from smallest or largest
        - build frequency map

        cur = min
        if min exist:
            reduce from counter
            update cur++
            repeat until build new group

        '''
        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)
        '''
        1: 1
        2: 2
        3: 2
        4: 2
        5: 1
        '''

        while freq:
            cur = min(freq.keys())
            
            # Decrease count for the start of the group               
            for _ in range(groupSize):
                if freq.get(cur, 0) > 0:
                    freq[cur] -= 1
                    if freq[cur] == 0:
                        del freq[cur]
                    cur += 1
                else:
                    return False

        return True