from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    dict_frequency = {}
    for e in nums:
        if e in dict_frequency:
            dict_frequency[e] += 1
        else:
            dict_frequency[e] = 1
    return list(dict(sorted(dict_frequency.items(), key=lambda item: item[1])).keys())[-k:]

print(topKFrequent ([1], 1))