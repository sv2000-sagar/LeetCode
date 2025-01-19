# Time: O(n×groupSize)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand) % groupSize != 0):
            return False
        count = {}
        for c in hand:
            count[c] = count.get(c,0) + 1
        for card in sorted(count):
            while(count[card] > 0): # freq of same card(num)
                for i in range(card, card+groupSize):
                    if(i not in count or
                       count[i] <= 0):
                        return False
                    count[i] -= 1
        return True      