# Time: O(m*n*4^L)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self,word):
        cur = self
        for c in word:
            if(c not in cur.children):
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the Trie
        root = TrieNode()
        for w in words:
            root.addWord(w)

        rows,cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r,c,node,word):
            # Return if out of bounds, already visited, or the letter not in Trie
            if(r < 0 or c < 0 or
               r >= rows or c >= cols or
               (r,c) in visit or
               board[r][c] not in node.children):
               return

            visit.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]] # Update the current node
            if(node.endOfWord == True):
                res.add(word) # Add the word to the result if it's valid

            # Explore all directions
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))  # Backtrack

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)