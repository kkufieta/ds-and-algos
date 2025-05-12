from lib import trie

def find_strings(grid, words):
  if len(grid) == 0 or len(grid[0]) == 0 or len(words) == 0:
    return []
  
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

def find_words(grid, r, c, node, s, t):
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

  for r_, c_ in valid_neighbors(r, c):
    ch = grid[r_][c_]
    if ch in node.children:
        grid[r_][c_] = None
        found_words.extend(find_words(grid, r_, c_, node.children[ch], s+ch, t))
        grid[r_][c_] = ch
  return found_words