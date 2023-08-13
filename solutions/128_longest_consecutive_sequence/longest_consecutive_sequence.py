
def longestConsecutive(nums) -> int:
    if not nums:
        return 0

    nums = set(nums)
    longest = 1

    for num in nums:
        if num - 1 not in nums:
            curr = num
            curr_longest = 1

            while curr + 1 in nums:
                curr += 1
                curr_longest += 1

            longest = max(longest, curr_longest)
    
    return longest

print(longestConsecutive([]))