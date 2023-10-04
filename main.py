from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    index = None
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                index = [i, j]
                break
    return index

if __name__ == "__main__":
    print(twoSum([3,2,4],6))
