class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """

    def searchInsert(self, A, target):
        # write your code here
        if not A:
            return 0

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return end + 1
