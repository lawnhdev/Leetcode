class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        String forwards = Integer.toString(x);
        String backwards = "";
        while (x >= 10) {
            int currDigit = x % 10;
            backwards += currDigit;
            x /= 10;
        }
        backwards += x;
        return backwards.equals(forwards);
    }
}