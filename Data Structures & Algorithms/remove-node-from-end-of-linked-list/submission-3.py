# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0 if head == None else 1
        node = head

        while node.next != None:
            node = node.next
            length +=1
        
        curr = head

        #Deleting single node
        if n == 1 and head.next == None:
            return None 

        #Deleting first node
        if (length - n) == 0:
            return head.next

        i=0
        while i != (length - n -1):
            curr = curr.next
            i+=1

        #Deleting last node
        if curr.next.next == None:
            curr.next = None
        #Deleting mid node
        else:    
            tmp = curr.next.next
            curr.next = tmp
            
        return head
        
            