class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        same letters, with same quantities

        traverse the first string
        
        make a dict
        ba aa
        a: 0

        value are all 0, say its is an anagram

        if value is 0, delete the item
        check the hashmap size, if 0 return true

        aaccerr aaccerr

        racecar
        r: 2
        a: 2
        c: 2
        e: 1

        carrace

        aa

        aaa

        ab aa
        b: 1

        a bbbbbb
        '''
        if len(s) != len(t):
            return False

        map = {}
        
        # traverse the first string
        for i in range(len(s)):
            key = s[i]
            if key in map:
                map[key] += 1
            else:
                map[key] = 1

        # traverse the second string
        for i in range(len(t)): #enumerate, give index and character
            currentChar = t[i]
            if currentChar in map:
                # if value is 0, delete the item
                if map[currentChar] == 1:
                    del map[currentChar]
                else:
                    # decrement the value
                    map[currentChar] -= 1
            else: # currentChar is no more left in map, cutting it short
                return False

        return len(map) == 0

            

        

    



        