from .ll_merge import merge_lists


def test_simple_merge_true(ll1, ll2):
    '''
    test for merging two linked list and
    assert its return head value
    '''

    head = merge_lists(ll1, ll2)
    assert head.val == 1


def test_merge_ll1_only_head(ll1_one, ll2):
    '''
    test to confirm if the merge_lists function
    breaks, and not runs into exception, and return the head of linked-list1
    when ll1 has only one node.
    '''

    head = merge_lists(ll1_one, ll2)
    assert ll1_one._len == 1
    assert head.val == 1


def test_merge_head_next_value_check(ll1, ll2):
    '''
    test to confirm if the value of node next to the result head
    is the value of head of ll2. this confirms if the merge is occuring
    as alternative order.
    '''
    head = merge_lists(ll1, ll2)
    assert head._next.val == ll2.head.val
