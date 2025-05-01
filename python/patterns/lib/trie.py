
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

    def _search_prefix_node(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, string):
        node = self._search_prefix_node(string)
        return node != None and node.is_word

    def search_prefix(self, string):
        node = self._search_prefix_node(string)
        return node != None

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

