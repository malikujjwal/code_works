# start with node as 0 to skip none condition
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        current = head
        
        while n > 0:
            current = current.next
            n -= 1
            
        skipNode = dummy
        while current:
            current = current.next
            skipNode = skipNode.next
        
        skipNode.next = skipNode.next.next
        
        return dummy.next