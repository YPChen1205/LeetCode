class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root={'*':'*'}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current['*'] = '*'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for c in word:
            if c not in current:
                return False
            current = current[c]
        return '*' in current

    def startsWith(self, prefix: str)  -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for c in prefix:
            if c not in current:
                return False
            current = current[c]
        return True
