class WordDictionary:

    """
    man i got tled ill do this when i know tries.
    """

    def __init__(self):
        self.wd = {}

    def addWord(self, word: str) -> None:
        self.wd[word] = 1

    def search(self, word: str) -> bool:
        if word in self.wd: return True
        if "." not in word: return False

        for k in self.wd:
            l = len(k)
            if l != len(word): continue
            for i in range(l):
                if i == l-1 and (word[i] == k[i] or word[i] == "."):
                    return True
                if word[i] == k[i]: continue
                elif word[i] == ".": continue
                else: break

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
