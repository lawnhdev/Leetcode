class Solution {
    public String mergeAlternately(String word1, String word2) {
        String ret = "";
        int word1length = word1.length();
        int word2length = word2.length();
        if (word1length > word2length) {
            for (int i = 0; i < word2length; i++) {
                ret += word1.charAt(i);
                ret += word2.charAt(i);
            }
            ret += word1.substring(word2length, word1length);
        } else  if (word2length > word1length){
            for (int i = 0; i < word1length; i++) {
                ret += word1.charAt(i);
                ret += word2.charAt(i);
            }
            ret += word2.substring(word1length, word2length);
        } else {
            for (int i = 0; i < word2length; i++) {
                ret += word1.charAt(i);
                ret += word2.charAt(i);
            }
        }
        return ret;
    }
}