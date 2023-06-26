def find_combinations(nums, target):
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
    for i in range(len(merged_array)):
        left = i + 1
        right = len(merged_array) - 1
        while left < right:
            current_sum = sum(merged_array[x] for x in range(i, left + 1)) + merged_array[right]
            if current_sum == doubled_target:
                combinations.append(merged_array[i:right+1])
                # Move the pointers to find other combinations
                left += 1
                right -= 1
            elif current_sum < doubled_target:
                left += 1
            else:
                right -= 1

    return pairs, merged_array, combinations

# Example usage
nums = [1, 3, 2, 2, -4, -6, -2, 8]
target = 4
pairs, merged_array, combinations = find_combinations(nums, target)

print("First Combination For", target, ":", pairs)
print("Merge Into a single Array:", merged_array)
print("Second Combination For", 2*target, ":", combinations)
