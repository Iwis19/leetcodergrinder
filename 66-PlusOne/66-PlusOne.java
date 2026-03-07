// Last updated: 3/6/2026, 9:31:37 PM
class Solution {
    public int[] plusOne(int[] digits) {
        for(int i = digits.length-1; i >= 0; i--){
            if(digits[i] + 1 <= 9){
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
 
        }
        int[] output = new int[digits.length+1];
        output[0] = 1;
        return output;
        
        
    }
}