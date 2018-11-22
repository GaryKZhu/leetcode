class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = ""
        n2 = ""
        while l1 != None:
            n1 = n1 + str(l1.val)
            l1 = l1.next
            
        while l2 != None:
            n2 = n2 + str(l2.val)
            l2 = l2.next
            
            
        sum = int(n1[::-1]) + int(n2[::-1])

        return list(reversed(list(map(int,str(sum)))))
        ##return list(map(int,str(sum)[::-1]))
