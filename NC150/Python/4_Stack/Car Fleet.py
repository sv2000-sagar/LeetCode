# Time: O(nlogn)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        stack = []
        # My
        for p,s in sorted(pair)[::-1]: #sorted in decreasing order
            time = (target - p)/s
            if(stack and time <= stack[-1]):
                continue
            stack.append(time)
        return len(stack)
        # NC
        # for p,s in sorted(pair)[::-1]: #sorted in decreasing order
        #     time = (target - p)/s
        #     stack.append(time)
        #     if(len(stack) >= 2 and stack[-1] <= stack[-2]):
        #         stack.pop()
        # return len(stack)