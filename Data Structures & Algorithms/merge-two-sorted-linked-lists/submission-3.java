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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {// list1 es de tamaño 1. list2 es de tamaño 2.
        
        // Optima
        ListNode mergedList = new ListNode(0);// add Dummy Node para poder 
        ListNode temp = mergedList;// temp apunta a mergedList

        // Time: O(n + m). Space: O(1)
        while(list1 != null || list2 != null) {
            if(list1 == null) {
                temp.next = list2;// mergedList.next = new ListNode(list2.val) (new ListNode(list2.val) es un nodo con atributo next)
                temp = temp.next;// recorrer el puntero al siguiente nodo (temp ahora a mergedList.next)
                list2 = list2.next;
                continue;
            } else if(list2 == null) {
                temp.next = list1;
                temp = temp.next;
                list1 = list1.next;
                continue;
            }


            if(list1.val == list2.val) {// Solo recorrer el puntero en una de las listas
                temp.next = list1;
                temp = temp.next;
                list1 = list1.next;
                //list2 = list2.next;
            } else if(list1.val < list2.val) {
                temp.next = list1;
                temp = temp.next;
                list1 = list1.next;
            } else { // list2.val < list1.val, es decir, list1.val > list2.val
                temp.next = list2;
                temp = temp.next;
                list2 = list2.next;
            }
        }

        return mergedList.next;
    }
}