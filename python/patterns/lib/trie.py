
class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        node = self.root
        for ch in string:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, string):
        node = self.root
        for ch in string:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def search_prefix(self, string):
        node = self.root
        for ch in string:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def remove_characters(self, string_to_delete):
        if not self.search(string_to_delete):
            return
        node = self.root
        child_list = []

        for c in string_to_delete:
            child_list.append((node, c))
            node = node.children[c]

        for parent, c in reversed(child_list):
            target = parent.children[c]
            if parent.children[c].children:
                return
            del parent.children[c]

