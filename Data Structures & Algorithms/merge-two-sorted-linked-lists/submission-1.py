# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #Avoids the problem of inserting into an empty list
        #Dummy is a placeholder that will be taken off from the return
        dummy = ListNode()
        newList = dummy

        while list1 and list2:
            #Check which list have the smaller head
            if list1.val < list2.val:
                #Append head to the tail of newList
                newList.next = list1
                #Update list 1
                list1 = list1.next
            else:
                #Append head to the tail of newList
                newList.next = list2
                #Update list 1
                list2 = list2.next
            #Advance the merged list pointer, so we compare the new node
            #in the next iteration
            newList = newList.next
        #Append the remaining list
        newList.next = list1 if list1 else list2
        #Return head skipping dummy
        return dummy.next
        