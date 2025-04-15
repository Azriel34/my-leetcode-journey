def sherlockAndAnagrams(s):
    counter = {}
    for i in range(len(s)):
        freq = [0]* 26
        for j in range(i,len(s)):
            char = s[j]
            freq[ord(char) - ord('a')] += 1
            key = tuple(freq)
            if key in counter:
                counter[key] += 1
            else:
                counter[key] = 1
        
        
    total =0
    for val in counter.values():
        if val>1:
         total+=(val*(val-1))//2
        
    return total
