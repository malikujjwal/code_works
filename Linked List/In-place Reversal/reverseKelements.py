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

def reverseKLinkedList(head, k):
    if k == 1:
        return head 
    
    nodeBeforeSplit, nodeAfterSplit, current = None, head, head
    previous, next = None, None
    headNode = None
    while True:
        i = 0

        while current is not None and i < k:
            next = current.next
            current.next = previous
            previous = current
            current = next 
            i += 1

        if nodeBeforeSplit is None:
            headNode = previous
            nodeBeforeSplit = nodeAfterSplit
        else:
            nodeBeforeSplit.next = previous 
            nodeBeforeSplit = nodeAfterSplit

        if current is None:
            nodeAfterSplit.next = None
            break
        else:
            nodeAfterSplit = current        

    return headNode

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.printList()
    head = reverseKLinkedList(head, 2)
    head.printList()

main()