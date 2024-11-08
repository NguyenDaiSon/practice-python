class Solution:
    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        min_banana = 1
        max_banana = max(piles)
        min_speed = -1
        while min_banana <= max_banana:
            bananas = min_banana + (max_banana - min_banana) // 2
            if self.canFinishEating(piles, hours, bananas):
                min_speed = bananas
                max_banana = bananas - 1
            else:
                min_banana = bananas + 1
        return min_speed

    def canFinishEating(self, piles: List[int], hours: int, bananas: int) -> bool:
        hours_used = 0
        for pile in piles:
            hours_used += (pile + bananas - 1) // bananas
            if hours_used > hours:
                return False
        return hours_used <= hours
