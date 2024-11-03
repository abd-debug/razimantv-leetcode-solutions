# Split a string into the max number of unique substrings

[Problem link](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        def work(i, used):
            if i == n:
                return 0
            ret = -n
            for j in range(i, n):
                cur = s[i:j+1]
                if cur not in used: 
                    used. append(cur)
                    ret = max(ret, work(j + 1, used) + 1)
                    used.pop()
            return ret
        return work(0, [])
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking) > [Push and pop for efficient state update](/Collections/backtracking.md#push-and-pop-for-efficient-state-update)