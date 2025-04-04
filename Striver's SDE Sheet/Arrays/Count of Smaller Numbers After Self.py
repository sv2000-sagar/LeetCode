# Striver (Count Inversions)
# Time: O(nlogn)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        enum = list(enumerate(nums))  # (index, value)

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left_half = merge_sort(arr[:mid])
            right_half = merge_sort(arr[mid:])
            return merge(left_half, right_half)

        def merge(left, right):
            result = []
            i = j = 0
            right_counter = 0  # number of smaller elements moved from right to result
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    # left[i] is greater than right_counter elements from right
                    count[left[i][0]] += right_counter
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    right_counter += 1
                    j += 1
            # Remaining left items also get right_counter
            while i < len(left):
                count[left[i][0]] += right_counter
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1
            return result
        
        merge_sort(enum)
        return count