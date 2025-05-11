class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = {}
        for n in nums2:
            while(stack and stack[-1] < n):
                res[stack.pop()] = n
            stack.append(n)
        ans = []
        for n in nums1:
            ans.append(res.get(n,-1))
        return ans