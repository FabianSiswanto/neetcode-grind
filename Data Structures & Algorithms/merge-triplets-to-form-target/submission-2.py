class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        max of both triplets

        bruteforce: check all triplets combinations -> nC2 -> poly time

        can merge triplets multiple times

        early terminate if element at index a/b/c from target not found in triplets

        will hit edge case (max might override some stuff):
        create 3 sets -> a,b,c
        find if target in there

        actual approach:
        filter out useless stuff -> triplets with value higher than target
        check if element matches target
        '''
        isFound = [False] * 3

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue # is useless triple

            for i,v in enumerate(t):
                if t[i] == target[i]:
                    isFound[i] = True
                    if all(isFound):
                        return True
        
        return False

        