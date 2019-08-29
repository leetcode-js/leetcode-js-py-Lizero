# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, s=0) -> ListNode:
        newSum = l1.val + l2.val + s
        l1.val = newSum % 10
        if (l1.next or l2.next):
            l1.next = self.addTwoNumbers(l1.next or ListNode(
                0), l2.next or ListNode(0), newSum//10)
        elif newSum >= 10:
            l1.next = ListNode(1)
        return l1


def makeListNode(l):
    s = ListNode(l[0])

    n = s
    for i in l[1:]:
        n.next = ListNode(i)
        n = n.next

    return s


def printListNode(l):
    s = [l.val]
    while l.next:
        l = l.next
        s.append(l.val)
    return s


if __name__ == '__main__':
    s = Solution()
    addTwoNumbers = s.addTwoNumbers

    l1 = makeListNode([2, 4, 3])
    l2 = makeListNode([5, 6, 4])

    l = addTwoNumbers(l1, l2)

    print(printListNode(l) == [7, 0, 8])
