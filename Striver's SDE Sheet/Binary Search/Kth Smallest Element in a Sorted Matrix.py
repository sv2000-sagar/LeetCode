class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        def upperBound(arr: List[int], x: int) -> int:
            l, r = 0, len(arr) - 1
            res = len(arr)
            while l <= r:
                mid = (l + r) // 2
                if x < arr[mid]:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return res

        def countSmallEqual(x: int) -> int:
            cnt = 0
            for i in range(m):
                cnt += upperBound(matrix[i], x)
            return cnt

        low = min(row[0] for row in matrix)
        high = max(row[-1] for row in matrix)
        req = k - 1

        while low <= high:
            mid = (low + high) // 2
            if countSmallEqual(mid) <= req:
                low = mid + 1
            else:
                high = mid - 1

        return low
