class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        approach1:
        p1, p2 for each word

        if one of pointer goes out of bounds -> append the rest of other word

        approach2:
        take min of len of both words -> add to res
        append rest
        '''
        min_len = min(len(word1), len(word2))
        res = []

        for i in range(min_len):
            res.append(word1[i])
            res.append(word2[i])

        # at most one will fire
        res.append(word1[min_len:])
        res.append(word2[min_len:])

        return "".join(res)
