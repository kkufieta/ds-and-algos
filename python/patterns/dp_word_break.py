from collections import defaultdict

# TODO[kat]: Once the kk/trie branch is merged, remove this and import the library
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

# TODO[kat]: Once the kk/trie branch is merged, remove this and import the library
class Trie:
    def __init__(self, words=[]):
        self.root = TrieNode()
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

def word_break(s, word_dict):
    t = Trie(word_dict)
    sentences = defaultdict(list)

    def find_words(idx):
        if idx in sentences:
            return
        node = t.root
        for i in range(idx, len(s)):
            if s[i] not in node.children:
                return
            if node.children[s[i]].is_word:
                if i == len(s) - 1:
                    sentences[idx].append(s[idx:])
                    return
                find_words(i+1)
                if i+1 in sentences:
                    prefix = s[idx:i+1] + " "
                    for postfix in sentences[i+1]:
                        sentences[idx].append(prefix + postfix)
                    del sentences[i+1]
            node = node.children[s[i]]

    find_words(0)
    return sentences[0]