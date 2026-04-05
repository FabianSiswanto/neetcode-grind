class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        function backtrack(index) -> what are the sentences that can be built from this index
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

        def backtrack(i: int) -> List[str]:
            if i in cache:
                return cache[i]

            if i == len(s):
                return [""]

            res = []
            for j in range(i, len(s)):
                cur_word = s[i: j + 1]
                if cur_word not in word_set:
                    continue

                # part of word_set
                remaining_sentences = backtrack(j + 1)
                if not remaining_sentences:
                    continue
                    
                for remaining_sentence in remaining_sentences:
                    sentence = cur_word
                    if remaining_sentence:
                        sentence += " " + remaining_sentence
                    res.append(sentence) # TODO: WHY IS THIS A VALID SENTENCE

            cache[i] = res
            return res

        return backtrack(0)

        


