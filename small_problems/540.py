class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left_pos, right_pos = 0, len(nums) - 1
        result_pos = 0

        while left_pos <= right_pos:
            middle_pos = left_pos + (right_pos - left_pos) // 2
            if self.moveLeft(nums, middle_pos):
                result_pos = middle_pos
                right_pos = middle_pos - 1
            else:
                left_pos = middle_pos + 1

        return nums[result_pos]

    def moveLeft(self, nums: List[int], index: int) -> bool:
        if index == len(nums) - 1:
            return True

        if index % 2 == 1:
            return nums[index] != nums[index - 1]

        return nums[index] != nums[index + 1]
