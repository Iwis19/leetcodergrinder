class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        current_string = set()
        max_length = 0
        left = 0

        for right in range(len(s)):

            char = s[right]
            while char in current_string:
                current_string.remove(s[left])
                left += 1
            
            current_string.add(char)
            max_length = max(right - left + 1, max_length)

        return max_length


        """
        do not entirely reset the string, only remove up until when the prev dupe character is gone
        """
