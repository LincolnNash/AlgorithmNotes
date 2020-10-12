class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
head = ListNode(0)
a = ListNode(1)
b = ListNode(2)
head.next = a
a.next = b


def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    def isPalindrome(self, head):
        lnode = ListNode(0)
        lnode.next = head
        if lnode.next is None:
            return True
        # 寻找中间节点
        mid = lnode
        rear = lnode
        count = 0
        while True:
            if rear.next is not None:
                rear = rear.next
                count += 1
            else:
                break
            if rear.next is not None:
                rear = rear.next
                count += 1
            mid = mid.next
        mid0 = mid.next
        if mid0 == None:
            return True
        # 反转前半段链表
        p1 = lnode.next
        p2 = p1.next
        while p1 != mid:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        if count % 2 != 0:
            mid = mid.next
        # 对比
        ans = True
        while mid != None and mid0 != None:
            if mid.val != mid0.val:
                ans = False
                break
            mid = mid.next
            mid0 = mid0.next
        return ans

print(isPalindrome(head))