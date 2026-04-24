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
        slow.next = null;// INSIGHT: first half saved. "second" remains having the object slow.next. This at the same time makes the head now it has only its first half
        ListNode prev = null;

        while(second != null) {// second = current
            ListNode next = second.next;

            second.next = prev;// next remains with the previous value of second.next
            prev = second;

            second = next;
        }// prev is the reverse of second half (second) of head

        // 3. Merge both lists
        ListNode first = head; // 2 -> 4 -> null 
        second = prev;// 8 -> 6 -> null
        while(second != null) {
            ListNode temp1 = first.next;// 4 -> null | null
            ListNode temp2 = second.next;// 6 -> null | null

            first.next = second;// first = 2 -> ([8] -> 6 -> null), | first.next* = 4 -> ([6] -> null)
            second.next = temp1;// 8 -> ([4] -> null),... first = 2 -> 8 -> 4 -> null | first.next* = 4 -> 6 -> (null)

            first = temp1; // first apunta ahora a temp1 (que es el mismo next de first "first.next") = 4 -> null | null
            second = temp2;// 6 -> null | null

        }// next* indicates 


    }
}
