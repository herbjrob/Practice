wordsDict = {}
freq = {}
        
# O(N) where N is the number of Words
for i in words:
	if i not in wordsDict:
        	wordsDict[i] = 1
        else:
                wordsDict[i] += 1
        
# O(N) where N is the number of unique words
for i in wordsDict:
	if wordsDict[i] not in freq:
        	freq[wordsDict[i]] = [i]
        else:
                freq[wordsDict[i]] += [i]
        
keys = freq.keys()
highest = max(keys)
        
ans = []
        
# O(N) where N is the different frequencies
while highest > 0:
	if highest in freq:
        	temp = freq[highest]
                temp.sort() # O(N logN) where N is the number of words at that frequency
                ans += temp
        highest -= 1