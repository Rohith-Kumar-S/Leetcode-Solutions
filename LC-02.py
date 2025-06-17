# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        arr = []
        while True:
            a,b = 0, 0
            if l1: 
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2= l2.next
            sum = a + b + carry
            carry = 0
            if sum >= 10:
               val = sum % 10
               carry = (sum - val) // 10
               sum = val
            arr.append(sum)     
            if not l1 and not l2 and carry==0:
                break
        out = None
        for val in arr[::-1]:
            if not out:
                out = ListNode(val=val , next=None)
            else:
                out = ListNode(val=val , next=out)
        return out

        
                
                
            

if __name__ == "__main__":
    l1 = ListNode(val=0 , next=None)
    l2 = ListNode(val=9 , next=ListNode(val=9 , next=None))
    out = Solution().addTwoNumbers(l1, l2)
    
    while True:
        print(out.val)
        out = out.next
        if not out:
            break
    
    