class Solution:
    def removeDuplicateLetters(self, string: str) -> str:

        """
        indeed same as 1081, wont come back to this will jsut do 1081

        3 ms runtime beats 64%
        """
         
        freq = Counter(string)  # turns a string into a dict w all of its letters, NEW SYTNAX FOR ME!!!
        stack, stack_seen = [], set()

        for char in string:

            freq[char] -= 1

            if char in stack_seen: continue

            while stack and char < stack[-1] and freq[stack[-1]]:  # doesnt need to be char <= stack[-1] because the possibility of == is gone since if its seen then its continued
                stack_seen.remove(stack.pop()) # -> .pop() returns the val

            stack.append(char)
            stack_seen.add(char)

        return "".join(stack)

            
