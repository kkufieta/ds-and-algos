class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def _append_sentences(self, s, suffixes, prefix_idx, suffix_idx):
        for suffix in suffixes[suffix_idx]:
            suffixes[prefix_idx].append(s + " " + suffix)


    def get_sentences(self, suffixes, s, idx):
        node = self.root
        # Need: s, idx, dict w/ index -> suffixes
        suffixes[idx] = []
        for i, ch in enumerate(s):
            if ch not in node.children:
                return
            node = node.children[ch]
            if node.is_word:
                if i == len(s) - 1:
                    suffixes[idx].append(s)
                    return
                if (idx + i + 1) not in suffixes:
                    self.get_sentences(suffixes, s[i+1:], idx + i + 1)
                if len(suffixes[idx + i + 1]) > 0:
                    self._append_sentences(s[:i+1], suffixes, idx, idx + i + 1)

def word_break(s, word_dict):
    t = Trie()
    for word in word_dict:
        t.add_word(word)

    sentences = {}
    t.get_sentences(sentences, s, 0)
    
    return sentences[0]