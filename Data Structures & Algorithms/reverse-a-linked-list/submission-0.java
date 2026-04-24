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


        Deque<Integer> stack = new ArrayDeque<>();// LIFO (LastIn - FirstOut)

        ListNode list = head;
        while(list != null) {
            stack.push(list.val);
            list = list.next;
        }

        ListNode reverseLinkedList = new ListNode(0);// para empezar a construir
        ListNode temp = reverseLinkedList;

        // 3. Vaciamos el stack (LIFO: saldrán 3, 2, 1, 0)
        while(!stack.isEmpty()) {
            temp.next = new ListNode(stack.pop());
            temp = temp.next;
        }

        return reverseLinkedList.next; 
    }


    
}
