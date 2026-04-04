class Solution:
    def intToRoman(self, num: int) -> str:

        """
        1. could not do this on my first try on my own. used a dict but was restricted since i cant iterate through 
        dictionary as its unordered

        2. now with an array from increasing val to decreasing, i can properly cycle thru hte max value, and this
        sticks now :)

        0 ms runtime 100
        """
        
        numbers = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10,"X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        
        res = []

        for i, number in enumerate(numbers):
            
            value = number[0]
            symbol = number[1]

            while num >= value:
                num -= value
                res.append(symbol)
            
        return "".join(res)



