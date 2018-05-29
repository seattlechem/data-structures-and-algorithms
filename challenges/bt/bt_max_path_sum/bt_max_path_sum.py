"""
Finding max path sum in a binary tree.

:res is result
:find_max() is a function to find max value.
:max_path_sum() is a  function to find what is max sum out of all paths.

"""
# at first define the res (result) as None
res = None


def find_max(root):
    """Max value will be found from this function."""
    # accessing global variable res
    global res
    # first if root is None
    if root is None:
        return 0
    max_l = find_max(root.left)
    max_r = find_max(root.right)
    # compare which value is greater, either from left or right + root, or
    # root itself
    max_s = max(max(max_l, max_r) + root.val, root.val)
    # compare either either path, root itself or left+root+right
    max_t = max(max_s, max_l + max_r + root.val, root.val)

    # now time to find max
    # if there is no previous res
    if res is None:
        # res will be always max_t b/c max_t is greatest value
        res = max_t
    else:
        # if previous res value is there
        # compare previous res and max_t
        res = max(res, max_t)
    # when return max value, will choose only one path: either left or right
    # that is why return max_s instead of max_t
    return max_s


def max_path_sum(root):
    """Find what is max path sum."""
    # invoke find_max()
    find_max(root)
    return res
