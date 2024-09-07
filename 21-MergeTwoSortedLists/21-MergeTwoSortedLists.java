/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        //ListNode list3 = new ListNode();
        if (list1 == null && list2 == null) { return null; }
        ListNode res = new ListNode();
        ListNode head = res;
        //list3 = new ListNode(1, new ListNode());
        //list3.val = 1;
        //list3.next = new ListNode();
        //list3 = list3.next;
        //list3 = new ListNode(2, new ListNode());
        //list3.val = 2;
        //list3.next = new ListNode();
       // list3 = list3.next;
       // list3 = new ListNode(4);
        //list3.val = 4;
        //list3.next = null;
        //return res;
        //System.out.println(res);
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                res.val = list1.val;
                res.next = new ListNode();
                list1 = list1.next;
            } else {
                res.val = list2.val;
                res.next = new ListNode();
                list2 = list2.next;
            }
            res = res.next;
        }
        if (list1 == null) {
            // append the rest of list 2 to res
            res.val = list2.val;
            res.next = list2.next;
            return head;
        } else if (list2 == null) {
            // append the rest of list 1 to res
            res.val = list1.val;
            res.next = list1.next;
            return head;
        } else {
            return head;
        }
    }
}