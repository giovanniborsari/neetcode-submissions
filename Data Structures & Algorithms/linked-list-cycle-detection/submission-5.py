# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #Empty list return false
        if not head:
            return False
        
        slow = head
        fast = head.next

        #If it is a single node return false
        if not slow.next:
            return False

        #Iterate until fast.next is None, end of list
        while fast.next != None:
            #If slow and 
            if slow == fast:
                return True
            #If slow gets to be None return False
            #Prevents exceptions
            if slow.next:
                slow = slow.next
            else:
                break
            #If fast gets to be None return False
            #Prevents exceptions
            if fast.next.next:
                fast = fast.next.next
            else:
                break
            
        return False
