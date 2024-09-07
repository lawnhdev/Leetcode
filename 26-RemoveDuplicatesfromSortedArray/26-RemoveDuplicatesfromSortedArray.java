class Solution {
    public int removeDuplicates(int[] nums) {
        Set<Integer> set = new LinkedHashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        System.out.println(set);
        int[] newArray = new int[set.size()];
        int index = 0;
        for (int num : set) {
            //System.out.println(num);
            //System.out.println(index);
            newArray[index] = num; 
            //System.out.println(newArray[index]);
            //System.out.println(index);
            index++;
        }
        //nums = newArray.clone();
        System.arraycopy(newArray, 0, nums, 0, newArray.length);
        return set.size();
    }
}