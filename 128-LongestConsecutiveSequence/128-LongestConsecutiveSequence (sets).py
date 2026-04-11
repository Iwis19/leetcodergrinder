class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
        O(n) runtime with set

        1. needed some help on implementing this algorithm because i dont think i am very very proficient iwth sets i keep forgetting
        2. needed help understanding why im checking if num-1 not in nums_set, but now i get it since i only need to check ones where nums-1 doesnt exist -> meaning that nums is the start of the sequence

        43 ms runtime beats 85%
        """

        if not nums:
            return 0

        nums_set = set(nums)
        res = 1

        for num in nums_set:

            #i must start checking from the start of hte sequence, so:
            if (num-1) not in nums_set:
                current_num = num
                temp = 1

                while (current_num+1) in nums_set:
                    temp += 1
                    current_num += 1
                
                res = max(res, temp)
        
        return res
