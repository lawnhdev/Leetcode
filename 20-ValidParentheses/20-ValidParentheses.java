class Solution {
    public boolean isValid(String s) {
        if (s.length() == 1 || s.length() % 2 == 1) {
            return false;
        }
        // remove pairs
        while (s.contains("{}") || s.contains("[]") || s.contains("()")) {
            s = s.replace("{}", "");
            s = s.replace("()", "");
            s = s.replace("[]", "");
        }
        System.out.println(s);
        Map<String, String> matches = new HashMap<>();
        matches.put("(", ")");
        matches.put("{", "}");
        matches.put("[", "]");
        int leftIndex = 0;
        int rightIndex = s.length() - 1;
        String leftOver = "";
        while (leftIndex < rightIndex) {
            String leftChar = s.charAt(leftIndex) + "";
            String rightChar = s.charAt(rightIndex) + "";
            if (matches.containsKey(leftChar)) {
                if (matches.get(leftChar).equals(rightChar)) {
                    // for when the match is right next to each other
                    if (leftIndex == rightIndex - 1) {
                        s = s.substring(rightIndex + 1, s.length());
                    } else {
                        s = s.substring(leftIndex + 1, rightIndex);
                    }
                    leftIndex = 0;
                    rightIndex = s.length() - 1;
                } else {
                    rightIndex--;
                }
            } else {
                return false;
            }
        }
        if (leftIndex == rightIndex) {
            return false;
        } else {
            return true;
        }
    }
}