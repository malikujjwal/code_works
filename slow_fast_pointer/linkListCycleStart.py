class Node:
   def __init__(self, value, next=None):
      self.value = value
      self.next = next

def cycleLegth(head):
    current = head
    cycleLength = 0
    while True:
        current = current.next
        cycleLength += 1
        if current == head:
            return cycleLength

def getCycle(head):
    slow, fast = head, head
    cycleLength, count = 0, 0
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            cycleLength = cycleLegth(slow)
            break
    
    j = head
    slow, fast = head, head

    while cycleLength:
        fast = fast.next
        cycleLength -= 1

    while fast != slow:
        slow = slow.next
        fast = fast.next
        count += 1

    return (count+1)

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = head.next.next

    print(getCycle(head))

main()