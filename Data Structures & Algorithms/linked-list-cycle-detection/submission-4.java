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
    public boolean hasCycle(ListNode head) {// 1 -> 2-> 3 -> 4 -> luego vuelve a apuntar a 2
        
        ListNode slowPointer = head;
        ListNode fastPointer = head;

        // O(n)
        while(slowPointer != null && fastPointer != null) {

            slowPointer = slowPointer.next;
            fastPointer = fastPointer.next != null ? fastPointer.next.next : null;
            

            // si ambos apuntan a la misma referencia donde se almacena el nodo, es una linked list cycle
            if(slowPointer != null && fastPointer != null && slowPointer == fastPointer) {// [2]* == [3] | [3]* == [2] | [4]* == [4]
                return true;
            }

            
            
            
        }

        return false;

    }
}
