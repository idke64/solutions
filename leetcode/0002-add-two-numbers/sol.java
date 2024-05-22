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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int c1 = 1;
        int c2 = 1;

        ListNode curr1 = l1;
        ListNode curr2 = l2;
        while (curr1.next != null){
            curr1 = curr1.next;
            c1++;
        }
        while (curr2.next != null){
            curr2 = curr2.next;
            c2++;
        }
        if (c1 >= c2){
            curr1 = l1;
            curr2 = l2;
        }
        else{
            curr1 = l2;
            curr2 = l1;
        }
        
        String ans = "";
        int carryover = 0;
        boolean stop = false;
        while (curr1 != null){
            if (!stop){
                ans += (curr1.val + curr2.val + carryover) % 10;
                if (curr1.val + curr2.val + carryover > 9){
                    carryover = 1;
                }
                else{
                    carryover = 0;
                }
            }
            else{
                ans += (curr1.val + carryover) % 10;
                if (curr1.val + carryover > 9){
                    carryover = 1;
                }
                else{
                    carryover = 0;
                }
            }
            
            
            curr1 = curr1.next;
            if (curr2.next != null){
                curr2 = curr2.next;
            }
            else{
                stop = true;
            }
            
        }
        if (carryover == 1){
            ans += "1";
        }
        ListNode out = new ListNode(Character.getNumericValue(ans.charAt(ans.length() - 1)));
        for (int i = ans.length() - 2; i >= 0; i--){
            out = new ListNode(Character.getNumericValue(ans.charAt(i)), out);
        }
        return out;
    }
}