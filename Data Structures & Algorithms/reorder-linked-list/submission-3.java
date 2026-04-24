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
    public void reorderList(ListNode head) {// head = 2 -> 4 -> 6 -> 8
        
        if(head == null || head.next == null) return;

        // 1. Find the medium nodo using 2 pointers slow and fast
        ListNode slow = head;
        ListNode fast = head.next;
        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }// slow is the medium of head, head remains original values

        // 2. Reverse second half of head
        ListNode second = slow.next;// second has the object slow.next
        slow.next = null;// first half saved. second remains having the object slow.next
        ListNode prev = null;

        while(second != null) {// second = current
            ListNode next = second.next;

            second.next = prev;// next remains with the previous value of second.next
            prev = second;

            second = next;
        }// prev is the reverse of second half (second) of head

        // 3. Merge both lists
        ListNode first = head; // 2 -> 4 -> 6 -> 8
        second = prev;// 8 -> 6
        while(second != null) {
            ListNode temp1 = first.next;
            ListNode temp2 = second.next;

            first.next = second;// 2 -> 8,
            second.next = temp1;// 8 -> 4,... 2 -> 8 -> 4 | 

            first = temp1; // 
            second = temp2;// 6 -> null

        }


    }
}
