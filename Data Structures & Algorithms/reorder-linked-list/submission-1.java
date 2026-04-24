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
        
        if(head == null || head.next == null) return;

        // 1. Count list elements
        ListNode temp = head;
        int n = 0;
        // O(n)
        while(temp != null) {
            n++;
            temp = temp.next;
        }

        /*temp = head;// Comprobar que head sigue con su contenido original

        while(temp != null) {
            System.out.println("Hola: " + temp.val);
            temp = temp.next;// temp ahora apunta a next de head
        }

        return;*/
        
        
        // 2. Reversed list elements (que el actual apunte al anterior (en el ejemplo de abajo, que 6 apunte a su prev = 5... y el anterior a 5, es null (su prev = null)))
        ListNode reversedLinkedList = null;// prev
        ListNode curr = head;// head = 5 -> 6 -> null
        while(curr != null) {// prev = null, curr = 5, next = 6 | prev = 5, curr = 6, next = null
            ListNode node = new ListNode(curr.val);

            node.next = reversedLinkedList;
            reversedLinkedList = node;            

            curr = curr.next;
        }

        /*temp = head;

        while(temp != null) {
            System.out.println("Hola: " + temp.val);
            temp = temp.next;
        }*/

        /*temp = reversedLinkedList;

        while(temp != null) {
            System.out.println("Hola: " + temp.val);
            temp = temp.next;
        }*/

        

        // 3. Build de list with size 7 containing elements of head and its reverse (reversedLinkedListHead)
        // O(n/2)
        ListNode reorderedList = new ListNode(0);// dummy node
        curr = head;
        temp = reorderedList;// Desde temp, construir reorderedList
        
        int i = 0;
        while(i < n) {
            temp.next = new ListNode(curr.val);
            temp = temp.next;
            curr = curr.next;
            
            i++;

            if(i < n) {
                temp.next= new ListNode(reversedLinkedList.val);
                temp = temp.next;
                reversedLinkedList = reversedLinkedList.next;
                i++;
            }
            

        }

        /*temp = head;// Comprobar que head sigue con su contenido original 
        while(temp != null) {
            System.out.println("cHola: " + temp.val);
            temp = temp.next;
        }*/

        // Copy of the content reorderedList to head
        temp = reorderedList.next;
        ListNode p1 = head;// p1 modifica a head
        while(temp != null) {

            System.out.println("Hola: " + temp.val);

            p1.val = temp.val;
            temp = temp.next;
            p1 = p1.next;
        }

        


    }
}
