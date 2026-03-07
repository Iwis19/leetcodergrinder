class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1:
            return 1 

        max_length = 0
        current_length = 0
        current_string = ""
        for i in range(len(s)):
            if s[i] not in current_string:
                current_string += s[i]
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_string = s[i]
                current_length = 1
        return max_length
