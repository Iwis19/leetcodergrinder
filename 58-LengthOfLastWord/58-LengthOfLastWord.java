// Last updated: 3/6/2026, 9:31:38 PM
class Solution {
    public int lengthOfLastWord(String s) {
        String temp = s.trim();
        int i = temp.lastIndexOf(" ");
        return temp.length() - i - 1;
    }
}