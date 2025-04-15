def twoStrings(s1, s2):
    count1 ={}
    
    
    for i in range(len(s1)):
        char1 =s1[i]
        if char1 in count1:
            count1[char1]+=1
        else:
            count1[char1]=1
            
    for J in range(len(s2)):
        char2 = s2[J]
        if char2 in count1:
            return "YES"
        else:
            continue
            
    return "NO"
