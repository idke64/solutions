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
    public ListNode doubleIt(ListNode head) {
        ListNode rev = reverse(head);
        ListNode doubled = null;
        int carryover = 0;
        while (rev != null){
            doubled = new ListNode(((rev.val * 2) + carryover) % 10, doubled);
            if ((rev.val * 2) + carryover >= 10){
                carryover = 1;
            }
            else{
                carryover = 0;
            }
            rev = rev.next;
        }
        if (carryover == 1){
            doubled = new ListNode(1, doubled);
        }
        return doubled;

    }
    public static ListNode reverse(ListNode l){
        ListNode prev = null;
        ListNode curr = l;
        ListNode next = null;
        while (curr != null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
}