# Definition for singly-linked list.
# we assume that the definition for a ListNode is defined elsewhere with the structure:
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# NOTE: I was having problems with type definition errors, so for the sake of simplicity I made a solution
#       array called "output" and converted it to a linked list after the fact. This gives a O(n*n) time complexity
#       which can be improved to O(n) complexity if a linked list append function is defined instead

def arr_to_ll(input):
    head = ListNode(input[0])
    ptr = head

    for i in range(1,len(input)):
        new_node = ListNode(input[i])
        if i == 1:
            head.next = new_node
            continue
        else:
            ptr = head
            while(ptr.next):
                ptr = ptr.next
            ptr.next = new_node
    return head

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr1 = l1
        ptr2 = l2
        output = []
        carry = 0
        value = 0

        while(ptr1 and ptr2):

            value = ptr1.val + ptr2.val
            value += carry

            if(value >= 10):
                carry = 1
                value -=10
                output.append(value)
            else:
                output.append(value)
                carry = 0

            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        if(not ptr1): 
            #ptr1 ended
            if (not ptr2): 
                #both end at the same time, make output into linked list
                if(carry == 1):
                    output.append(carry)

                linked_output = arr_to_ll(output)
                return linked_output
            else: 
                #just ptr1 ended but ptr2 has more listed
                while(ptr2):
                    value = ptr2.val + carry
                    if(value >= 10):
                        carry = 1
                        value -=10
                        output.append(value)
                    else:
                        output.append(value)
                        carry = 0
                    ptr2 = ptr2.next
        elif(not ptr2): 
            #ptr2 ended but ptr1 has more elements
            while(ptr1):
                value = ptr1.val + carry
                if(value >= 10):
                    carry = 1
                    value -=10
                    output.append(value)
                else:
                    output.append(value)
                    carry = 0
                ptr1 = ptr1.next

        if(carry == 1):
            output.append(carry)

        linked_output = arr_to_ll(output)
        return linked_output

        


        
        

            


        