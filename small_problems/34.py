class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstIndex = self.findIndex(nums, target, True)
        lastIndex = self.findIndex(nums, target, False)
        return [firstIndex, lastIndex]
    
    def findIndex(self, nums: List[int], target: int, firstIndex: bool) -> int:
        firstPos, lastPos = 0, len(nums) - 1
        expectedPos = -1
        while firstPos <= lastPos:
            middlePos = firstPos + (lastPos - firstPos)//2
            if target == nums[middlePos]:
                expectedPos = middlePos
                if firstIndex:
                    lastPos = middlePos - 1
                else:
                    firstPos = middlePos + 1
            elif target < nums[middlePos]:
                lastPos = middlePos - 1
            else:
                firstPos = middlePos + 1
        return expectedPos
        
