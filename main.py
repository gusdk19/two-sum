from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    num_indices = {}

    for index, num in enumerate(nums):
        complement = target - num

        # If the complement exists in our dictionary, return its index and the current index
        if complement in num_indices:
            return [num_indices[complement], index]

        # Otherwise, store the current number's index in the dictionary
        num_indices[num] = index

    # If no solution is found, return an empty list
    return []