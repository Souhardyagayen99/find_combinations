def find_combinations(nums, target):
    def backtrack(nums, temp, curridx, cur_sum, target, output):
        if cur_sum == target:
            output.append(temp.copy())
            return

        if cur_sum > target or curridx >= len(nums):
            return

        for i in range(curridx, len(nums)):
            if i > curridx and nums[i] == nums[i-1]:
                continue

            num = nums[i]
            temp.append(num)
            backtrack(nums, temp, i + 1, cur_sum + num, target, output)
            temp.pop()

    # Step 1: Find pairs that sum up to the target
    pairs = []
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append([num, complement])
        seen.add(num)

    # Step 2: Merge and sort the array
    merged_array = sorted(nums)

    # Step 3: Find combinations for the doubled target
    doubled_target = 2 * target
    combinations = []
    backtrack(merged_array, [], 0, 0, doubled_target, combinations)

    return pairs, merged_array, combinations

# Example usage
nums = [1, 3, 2, 2, -4, -6, -2, 8]
target = 4
pairs, merged_array, combinations = find_combinations(nums, target)

print("First Combination For", target, ":", pairs)
print("Merge Into a single Array:", merged_array)
print("Second Combination For", 2 * target, ":", combinations)
