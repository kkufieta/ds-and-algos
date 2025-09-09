from lib import trie

def find_strings(grid, words):
  t = trie.Trie()
  for w in words:
    t.insert(w)
    
  found_words = []
  for r, row in enumerate(grid):
    for c, ch in enumerate(row):
      if ch in t.root.children:
        grid[r][c] = None
        found_words.extend(find_words(grid, r, c, t.root.children[ch], ch, t))
        grid[r][c] = ch
  
  return found_words

def find_words(grid, row, col, node, s, t):
  found_words = []
  if node.is_word:
    found_words.append(s)
    t.remove_characters(s)
    if not t.search_prefix(s):
      return found_words

  valid_indices = lambda r, c: r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])
  valid = lambda r, c: valid_indices(r, c) and grid[r][c] != None
  neighbors = lambda r, c: [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
  valid_neighbors = lambda r, c: [n for n in neighbors(r, c) if valid(*n)]

  for r, c in valid_neighbors(row, col):
    ch = grid[r][c]
    if ch in node.children:
        grid[r][c] = None
        found_words.extend(find_words(grid, r, c, node.children[ch], s+ch, t))
        grid[r][c] = ch
  return found_words