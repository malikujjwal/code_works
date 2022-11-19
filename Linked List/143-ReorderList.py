# partition from middle and merge. 
class Solution(object):
    def reorderList(self, head):
        fastPointer, slowPointer = head.next, head
        
        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
        
        curr = slowPointer.next
        slowPointer.next = None
        prev, next = None, None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        firstHalf = head
        secondHalf = prev
        while secondHalf:
            tempPointer = firstHalf.next
            tempPointer2 = secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = tempPointer
            firstHalf, secondHalf = tempPointer, tempPointer2