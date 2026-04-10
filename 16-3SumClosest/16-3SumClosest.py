class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        """
        had a hard time thinking about the two pointers when i shouldve defaulted to it tbh, since all sum questi ons have been pointers

        1. good thing was that i definitely thought about keeping a closest_diff tracker, which was the right idea
        2. i initially did an extra check / call of the min function to minimize closest_diff, and then checked if the updated closest_diff is the new computed diff, so i could set answer and whatever, but it was very inefficient (costed me around 100 ms)
        3. mostly coded the solution myself, but still wondered why i didnt have to move the ptrs right after i update closest diff, but then i realized it could still be optimized thru the sum > tgarget, sum < target, sum == target checks, so no point and would be false if i moved

        343 ms runtime beats 85%
        """
        
        nums.sort()
        ans = 0
        closest_diff = math.inf

        for i in range(len(nums)-2):
            
            l,r = i+1, len(nums)-1
            goal = target - nums[i]

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                diff = abs(target - sum)
                if closest_diff > diff:
                    ans = sum
                    closest_diff = diff

                if sum == target:
                    return sum

                elif sum > target:
                    r -= 1
                
                elif sum < target:
                    l += 1
                
        return ans


