class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        function backtrack(index)
        -> check if end of str -> return arr of ""
        -> check cache

        try out all w combinations -> loop from i till len(s)
        -> if not in wordDict -> skip
        -> w in wordDict -> backtrack from next index -> store as strings

        -> if no strings -> continue
        -> go though all string in strings
            -> build sentences (starting from w) -> only do so if string has content
            -> append sentence to res
        
        save in cache
        return res

        call bactrack from index 0
        -> two types of returns: 
        '''
        word_set = set(wordDict)
        cache = {}
        res = []

        def backtrack(i: int) -> List[str]:
            if i in cache: # what is this
                return cache[i]

            if i == len(s):
                return [""]
                
            res = []
            for j in range(i, len(s)):
                cur_word = s[i: j + 1]
                if cur_word not in word_set:
                    continue
                # part of word_set
                other_words = backtrack(j + 1)
                for word in other_words:
                    sentence = cur_word
                    if word:
                        sentence += " " + word
                    res.append(sentence) # TODO: WHY IS THIS A VALID SENTENCE
            cache[i] = res

            return res

        return backtrack(0)

        


