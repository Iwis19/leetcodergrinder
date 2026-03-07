// Last updated: 3/6/2026, 9:31:39 PM
class Solution {
    public boolean isPalindrome(int x) {
        StringBuilder sb = new StringBuilder(Integer.toString(x));
        sb.reverse();



        if(Integer.toString(x).equals(sb.toString())){
            return true;
        }
        return false;
    }
}