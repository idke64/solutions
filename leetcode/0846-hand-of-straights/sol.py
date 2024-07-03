class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = 0
        m = {}
        for i in range(len(hand)):
            if hand[i] not in m:
                m[hand[i]] = 1
            else:
                m[hand[i]] += 1
        hand.sort()
        for i in range(len(hand) - 1, -1, -1):
            group = True
            for j in range(groupSize):
                if hand[i] - j not in m or m[hand[i] - j] <= 0:
                    group = False
                    break
            if group:
                count += 1
                for j in range(groupSize):
                    m[hand[i] - j] -= 1
        return count == len(hand) / groupSize
