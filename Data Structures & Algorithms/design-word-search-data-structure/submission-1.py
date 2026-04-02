class TrieNode:
    def __init__(self):
        self.children = {} #c: TrieNode
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.is_end = True
        

    def search(self, word: str) -> bool:
        '''
        if . -> try on all children -> dfs
        '''

        def dfs(j, root: TrieNode) -> bool:
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child): # try all child
                            return True
                    return False
                else: # normal case
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            
            return cur.is_end

        return dfs(0, self.root)
        
