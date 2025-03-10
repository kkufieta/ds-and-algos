from lib import trie

def find_strings(grid, words):
  if len(grid) == 0 or len(grid[0]) == 0 or len(words) == 0:
    return []
  
  t = trie.Trie()
  for w in words:
    t.insert(w)
    
  found_words = []
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      found_words.extend(backtrack(grid, row, col, t.root, "", t))
  
  return found_words

def backtrack(grid, row, col, node, word, t):
  found_words = []
  if node.is_word:
    found_words.append(word)
    t.remove_characters(word)

  last_row = len(grid) - 1
  last_col = len(grid[0]) - 1
  
  if row < 0 or row > last_row or col < 0 or col > last_col:
    return found_words
    
  if grid[row][col] == None:
    return found_words
    
  letter = grid[row][col]
  if letter in node.children:
    grid[row][col] = None
    for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
      if node == None or letter not in node.children:
        grid[row][col] = letter
        return found_words
      found_words.extend(backtrack(grid, r, c, node.children[letter], word+letter, t))
    grid[row][col] = letter
  return found_words