def merge_lists(ll1, ll2):
    '''
    Zip two linked lists together into one so that the nodes alternate \
    between the two lists and return a reference \
    to the head of the single list.
    '''
    current1 = ll1.head
    current2 = ll2.head
    if not current1:
        return current2
    if not current2:
        return current1

    while current1 and current2:
        temp1 = current1._next
        temp2 = current2._next
        current1._next = current2
        if not temp1:
            break
        current1 = temp1
        current2._next = current1
        current2 = temp2
        if not temp2:
            break
    return ll1.head
