// Last updated: 3/6/2026, 9:31:35 PM
class Solution {
    public boolean isHappy(int n) {   
        
        Set<Integer> seen = new HashSet<>();
        while (n != 1 && seen.add(n)) {
            n = algorithm(n);
        }
        return n == 1;
    }
    
    public int algorithm(int n){
        int output = 0;
        while(n > 0){
            int temp = n%10;
            output += temp*temp;
            n/=10;
        }
        return output;
    }
}

