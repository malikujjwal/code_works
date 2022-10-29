class Node:
    def __init__(self, value, next=None):
      self.value = value
      self.next = next
    
    def printList(self):
        temp = self
        while temp is not None:
            print (temp.value, end = " ")
            temp = temp.next
        print()

def reverseBetween(head, left, right):
    if left == right:
        return head
    
    previous, current = None, head
    i = 1
    while i < left:
        previous = current
        current = current.next
        i += 1
        
    lastNodeBeforeReversal = previous
    nodeAfterReversal = current
    
    i = 0
    next = None
    while current is not None and i < right-left+1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1
        
    if lastNodeBeforeReversal is not None:
        lastNodeBeforeReversal.next = previous
    else:
        head = previous
        
    nodeAfterReversal.next = current
    
    return head

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    head.printList()
    head = reverseBetween(head,2, 4)
    head.printList()

main()