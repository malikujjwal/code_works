class Solution(object):
    def copyRandomList(self, head):
        curr = head
        listRandomPairs = {None: None}
        
        while curr:
            copy = Node(curr.val)
            listRandomPairs[curr] = copy
            curr = curr.next
            
        curr = head
        
        while curr:
            copy = listRandomPairs[curr]
            copy.next = listRandomPairs[curr.next]
            copy.random = listRandomPairs[curr.random]
            curr = curr.next
            
        return listRandomPairs[head]