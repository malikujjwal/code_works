# start with empty node in python because node are passed as reference
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head
        
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next 
            else:
                current.next = list1
                list1 = list1.next
                
            current = current.next
            
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return head.next