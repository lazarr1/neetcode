class PrefixTree:

    class TrieNode:
        def __init__(self, char, final, word):
            self.val = char
            self.final = []
            if final:
                self.final = [word]
            
            self.next = [None for _ in range(26)]

        def insertWord(self, word):
            if word not in self.final:
                self.final.append(word)

    def __init__(self):
        self.roots = [None for _ in range(26)]

    def insert(self, word: str) -> None:
        insertList = self.roots
        insertIdx = ord(word[0]) - ord('a')

        i = 0
        while insertList[insertIdx] is not None:

            i+=1
            if i == len(word):
                break
            insertList = insertList[insertIdx].next
            insertIdx = ord(word[i]) - ord('a')

        if i == len(word):
            insertList[insertIdx].insertWord(word)
            return

        while i < len(word):
            
            insertList[insertIdx] = self.TrieNode(word[i], i == len(word) - 1, word)
            if i == len(word) - 1:
                insertList[insertIdx].insertWord(word)
                break
            insertList = insertList[insertIdx].next

            i+= 1
            insertIdx = ord(word[i]) - ord('a')

    def search(self, word: str) -> bool:
        insertList = self.roots
        insertIdx = ord(word[0]) - ord('a')
        
        i = 0
        while insertList[insertIdx] is not None:
            i+=1
            if i == len(word):
                break
            
            insertList = insertList[insertIdx].next


            insertIdx = ord(word[i]) - ord('a')            
            
        return i >= len(word) and insertList[insertIdx] is not None and word in insertList[insertIdx].final
        

    def startsWith(self, prefix: str) -> bool:
        insertList = self.roots
        insertIdx = ord(prefix[0]) - ord('a')

        i = 0
        while insertList[insertIdx] is not None and i < len(prefix):
            insertList = insertList[insertIdx].next
            i+=1
            if i == len(prefix):
                break
            insertIdx = ord(prefix[i]) - ord('a')

        return i == len(prefix)
        
        