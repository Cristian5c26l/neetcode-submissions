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
    public ListNode reverseList(ListNode head) {

        // Fuerza bruta: O(2n) = O(n) y O(n) en el espacio (por el stack)

        ListNode curr = head;
        ListNode prev = null;

        // O(n). Suponer la entrada "null -> [2] -> [3] -> null"... conseguir llegar a la siguiente iteracion con curr = 3, y prev = 2
        while(curr != null) {// Primera iteracion: prev = null, curr = 2.
            ListNode next = curr.next;
            curr.next = prev;// Esto es lo que invierte

            prev = curr;
            curr = next;
        }

        return prev; 
    }


    
}
