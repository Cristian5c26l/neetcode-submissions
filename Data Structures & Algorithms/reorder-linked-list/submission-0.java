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
        
        if (head == null || head.next == null) return;

        // 1. Clonar la lista original para no destruirla al invertir
        // (Esto es lo que faltaba para tu enfoque de "fuerza bruta")
        ListNode copyHead = new ListNode(head.val);
        ListNode copyTemp = copyHead;
        ListNode curr = head.next;
        int n = 1;
        
        while (curr != null) {
            copyTemp.next = new ListNode(curr.val);
            copyTemp = copyTemp.next;
            curr = curr.next;
            n++;
        }

        // 2. Invertir la copia (reversedLinkedListHead)
        ListNode prev = null;
        ListNode reverseCurr = copyHead;
        while (reverseCurr != null) {
            ListNode next = reverseCurr.next;
            reverseCurr.next = prev;
            prev = reverseCurr;
            reverseCurr = next;
        }
        ListNode reversedHead = prev;

        // 3. Reordenar la lista ORIGINAL modificando sus punteros .next
        // No creamos nodos nuevos aquí, re-enlazamos los existentes
        ListNode p1 = head;          // Puntero a la lista original
        ListNode p2 = reversedHead;  // Puntero a la lista invertida
        
        // Solo necesitamos iterar hasta la mitad (n/2)
        for (int i = 0; i < n / 2; i++) {
            ListNode nextP1 = p1.next;
            ListNode nextP2 = p2.next;

            p1.next = new ListNode(p2.val); // Usamos el valor de la invertida
            p1.next.next = nextP1;
            
            p1 = nextP1;
            p2 = nextP2;
        }

        // 4. Ajuste final: Cortar la lista en el elemento n
        // Para evitar ciclos infinitos, debemos terminar la lista en null
        curr = head;
        for (int i = 1; i < n; i++) {
            curr = curr.next;
        }
        curr.next = null;

    }
}
