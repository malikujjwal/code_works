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
    
def reverseLinkedList(head):
    previous, current, next = None, head, None

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    head.printList()
    head = reverseLinkedList(head)
    head.printList()

main()