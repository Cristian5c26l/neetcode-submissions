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
        Deque<Integer> stack = new ArrayDeque<>();// LIFO (LastIn - FirstOut)

        ListNode list = head;

        // O(n)
        while(list != null) {
            stack.push(list.val);
            list = list.next;
        }

        ListNode reverseLinkedList = new ListNode(0);// para empezar a construir... 0 seria el "Nodo cabecera"
        ListNode temp = reverseLinkedList; // temp apunta a reverseLinkedList (| [0] | -> )

        // O(n)
        while(!stack.isEmpty()) {// Primera iteracion: |[0] -> [3]|. Segunda iteracion: |[3] -> [2]|
            temp.next = new ListNode(stack.pop()); 
            temp = temp.next;// Apuntar al siguiente
        }

        return reverseLinkedList.next; 
    }


    
}
