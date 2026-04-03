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
    public void reorderList(ListNode head) {
        ArrayList<Integer> vals = new ArrayList<>();
        ListNode curr = head;

        while (curr != null) {
            vals.add(curr.val);
            curr = curr.next;
        }

        int i = 0; 
        int j = vals.size() - 1;
        boolean leftTurn = true;
        while (i <= j) {
            if (leftTurn) {
                head.val = vals.get(i);
                i++;
            }
            else {
                head.val = vals.get(j);
                j--;
            }
            leftTurn = !leftTurn;
            head = head.next;
        }

    }
}
