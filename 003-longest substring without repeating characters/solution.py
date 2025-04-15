class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen ={}
        maxs = 0
        start = 0

        for end in range(len(s)): # sliding window
            if s[end] in last_seen and last_seen[s[end]] >= start: # if we already saw this char
                start = last_seen[s[end]] + 1 #update sliding window start
            last_seen[s[end]] = end
            maxs = max(maxs, end - start +1)
        return maxs
