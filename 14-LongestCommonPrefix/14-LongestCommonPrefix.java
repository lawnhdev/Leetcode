class Solution {
    public String longestCommonPrefix(String[] strs) {
        String first = strs[0];
        while(true) {
            int truths = 0;
            for (int i = 0; i < strs.length; i++) {
                System.out.println(first);
                if (!strs[i].startsWith(first)) {
                    first = first.substring(0, first.length() - 1);
                } else {
                    truths++;
                }
            }
            System.out.println(truths);
            if (truths == strs.length || first.length() == 0) {
                return first;
            }
        }
    }
}