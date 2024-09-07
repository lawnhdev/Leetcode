class Solution {
    public int romanToInt(String s) {
        HashMap<String, Integer> map = new HashMap<>();
        int res = 0;
        int index = 0;
        map.put("I", 1);
        map.put("V", 5);
        map.put("X", 10);
        map.put("L", 50);
        map.put("C", 100);
        map.put("D", 500);
        map.put("M", 1000);
        map.put("IV", 4);
        map.put("IX",  9);
        map.put("XL", 40);
        map.put("XC", 90);
        map.put("CD", 400);
        map.put("CM", 900);
        for (int i = 0; i < s.length() - 1; i++) {
            String sub = s.charAt(i) + "" + s.charAt(i + 1);
            if (map.containsKey(sub)) {
                res += map.get(sub);
                i++;
            } else {
                String currChar = s.charAt(i) + "";
                res += map.get(currChar);
            }
            index = i;
        }
        if (index == 0 || index == s.length() - 2) {
            String lastChar = s.charAt(s.length() - 1) + "";
            res += map.get(lastChar);
        }
        return res;
    }
}