class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupings = {} # {'a':1, 'b':3} ==> index 
        output = []
        for word in strs:
            charFreqs = {}
            for char in word:
                charFreqs[char] = charFreqs.get(char, 0) + 1
            
            charFreqs = frozenset(charFreqs.items())
            if charFreqs in groupings:
                output[groupings[charFreqs]].append(word)
            else:
                groupings[charFreqs] = len(output)
                output.append([word])


        return output




            