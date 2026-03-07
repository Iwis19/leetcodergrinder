// Last updated: 3/6/2026, 9:31:36 PM
import java.math.BigInteger;

class Solution {
    public String addBinary(String a, String b) {
        return new BigInteger(a, 2).add(new BigInteger(b, 2)).toString(2);
    }
}
