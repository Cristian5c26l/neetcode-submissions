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

        // O(n). Suponer la entrada "null -> [2] -> [3] -> null"... conseguir llegar a la segunda iteracion con curr = 3, y prev = 2
        while(curr != null) {// Primera iteracion: prev = null, curr = 2.
            ListNode next = curr.next;// next = 3 -> null | next = null  
            curr.next = prev;// 2 (curr) -> (curr.next) null | 3 (curr) -> (curr.next = prev) 2 -> null Esto es lo que invierte

            prev = curr;// prev = (curr) 2 -> null | prev = 3 -> 2 -> null
            curr = next;// curr = 3 -> (curr.next) null |  curr = null
        }

        return prev; 
    }


    
}
