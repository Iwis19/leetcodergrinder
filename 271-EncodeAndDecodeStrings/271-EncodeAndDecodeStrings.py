class Solution:

    def encode(self, strs: List[str]) -> str:

        """
        did not solve on first submission, tried using delimiter but turned out i had to also include the length of the word.

        NOTE: its best to have delimiter after the length, as i can just pick up where i left off from i pointer all the way to j pointer, handling ANY digit for words length
        """

        encoded = ""
        for i, string in enumerate(strs):
            encoded+=f"{len(string)}/{string}"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        """
        if char is a delimiter(/), then i read the number (x) after it, and i take x subsequent characters, and add it
        to temp word, then to array, then go next word
        """
        temp_length = 0
        temp_word = ""
        while i < len(s):
            j = i
            while s[j] != "/":
                j+=1
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            i = j+1+length
        return decoded

