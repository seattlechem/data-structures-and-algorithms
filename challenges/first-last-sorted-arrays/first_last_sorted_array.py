"""Find first and last position of elements in sorted arrays."""

"""First and last position in sorted arrays."""


def searchRange(nums, target):
    """Find first and last position."""
    def midpoint(x, y):
        """Find mid point."""
        return x + (y - x) // 2

    lo, hi = 0, len(nums)-1
    _max = -1
    _min = float('inf')

    while lo <= hi:
        mid = midpoint(lo, hi)
        if nums[mid] == target:
            _max = max(_max, mid)
            _min = min(_min, mid)
        if nums[mid] <= target:
            lo = mid+1
        else:
            hi = mid-1

    if _max == -1:
        return [-1, _max]
    lo, hi = 0, _min

    while lo <= hi:
        mid = midpoint(lo, hi)
        if nums[mid] == target:
            _min = min(_min, mid)
        if nums[mid] >= target:
            hi = mid-1
        else:
            lo = mid+1
    return [_min, _max]
