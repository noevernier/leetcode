# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram**  is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:** 

```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2:** 

```
Input: s = "rat", t = "car"
Output: false
```

**Constraints:** 

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

**Follow up:**  What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# Solution

Type        |Abbr|Order|Replicates|   Math*   |   Python    | Implementation
------------|----|-----|----------|-----------|-------------|----------------
Set         |Set |  n  |     n    | {2  3  1} |  {2, 3, 1}  | set(el)
Ordered Set |Oset|  y  |     n    | {1, 2, 3} |      -      | list(dict.fromkeys(el)
Multiset    |Mset|  n  |     y    | [2  1  2] |      -      | <see `mset` below>
List        |List|  y  |     y    | [1, 2, 2] |  [1, 2, 2]  | list(el)