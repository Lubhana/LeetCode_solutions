
class Solution:
    def sum_up(self,node):
        current_node=node
        counter=1
        lst=[]
        while current_node:
            a=current_node.val*counter
            counter=counter*10
            lst.append(a)
            current_node=current_node.next   
        return sum(lst)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        solution_head=ListNode(0)
        current=solution_head
        l1_sumup=self.sum_up(l1)
        l2_sumup=self.sum_up(l2)
        res=l1_sumup+l2_sumup
        digits = []
        if res==0:
            return ListNode(0)

        while res > 0:
            digit = res % 10   
            digits.append(digit)  
            res = res // 10
        for num in digits:
            current.next=ListNode(num)
            current=current.next
        
        return solution_head.next

    