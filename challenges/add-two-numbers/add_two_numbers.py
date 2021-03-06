"""Two non-empty linked lists representing two non-negative integers are added."""


class ListNode():
    """ListNode class."""

    def __init__(self, x):
        """Instance of ListNode class."""
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """."""
    # create an instance of ListNode for return addition of two linked lists
    result = ListNode(0)
    # set the initial curr result linked list before branching out to next
    curr = result
    # since only one digit can be save on each node, define carry_over as var
    carry_over = 0

    while l1 or l2 or carry_over:
        # first add two linked lists including carry_over value
        val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry_over
        # only assign 10-digit number for carry_over
        carry_over = val // 10
        curr.next = ListNode(val % 10)
        curr = curr.next
        l1 = l1.next if l1.next else None
        l2 = l2.next if l2.next else None

    # reason why return result.next is because value added after initial 0
    return result.next

# Time: O(max(m, n)) where m and n represents the length of l1 and l2.
# Space: O(max(m, n))
