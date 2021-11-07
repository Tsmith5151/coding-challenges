""" 
Design Add and Search Words Data Structure

Reference:
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and finding if a string
matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.  void addWord(word) Adds word to the
data structure, it can be matched later.  bool search(word) Returns true if
there is any string in the data structure that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Solution = Trie (prefix trees)
Reference: https://www.youtube.com/watch?v=BTf05gs_8iU
"""


class TrieNode:
    """Trie (prefix tree) data structure"""

    def __init__(self):
        self.children = {}  # {char: TrieNode}
        self.word = False  # is a word


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            # if character is not inserted
            if c not in cur.children:
                # new trienode
                cur.children[c] = TrieNode()
            # update pointer to new trie node is does not exist
            cur = cur.children[c]
        cur.word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def dfs(j, root):
            """depth first search: recursive approach"""

            cur = root
            # iterate through each character in word
            for i in range(j, len(word)):
                c = word[i]
                # search thru 26 children
                if c == ".":
                    # use backtracking/recursion
                    for child in cur.children.values():
                        if dfs(i + 1, child):  # since we are skipping "."; +1 increment
                            return True
                        # if a match is not found:
                        else:
                            return False
                else:
                    # if character is not inserted then word if not found
                    if c not in cur.children:
                        return False
                    # update pointer to new trie node if does not exist
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)


if __name__ == "__main__":

    wordDictionary = WordDictionary()

    # Insert words
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")

    # Search for words
    # print('Searching...')
    # print("pad:", wordDictionary.search("pad")) # return False
    # print("bad:",wordDictionary.search("bad")) # return True
    print(".ad:", wordDictionary.search(".ad"))  # return True
    print("b..", wordDictionary.search("b.."))  # return True
