// Last updated: 3/6/2026, 9:31:39 PM
class Solution {
    public int romanToInt(String s) {
        int[] value = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbol = {"M", "CM","D", "CD","C", "XC","L", "XL","X", "IX","V", "IV","I"};

        int index = 0;
        int output = 0;

        while(index < s.length()){
            for(int j = 0; j < symbol.length; j++){
                if(s.startsWith(symbol[j], index)){
                    output += value[j];
                    index+=symbol[j].length();
                    break;
                }
            }
            
        }
        return output;
    }
}