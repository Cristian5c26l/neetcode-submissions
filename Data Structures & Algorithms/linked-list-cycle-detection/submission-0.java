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
    public boolean hasCycle(ListNode head) {
        // O(n) space
        Map<ListNode, Integer> nodeVisitesRegister = new HashMap<>();// Que la llave sea el nodo y no el val que contiene ya que los nodos pueden contener el mismo val

        ListNode pointer = head;

        // O(n)
        while(pointer != null) {

            if(nodeVisitesRegister.containsKey(pointer)) {
                return true;
            }

            nodeVisitesRegister.put(pointer, nodeVisitesRegister.getOrDefault(pointer, 0) + 1);
            pointer = pointer.next;
        }

        return false;

    }
}
