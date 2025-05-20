from collections import defaultdict

def compilation_order(dependencies):
    in_degree, graph = defaultdict(int), defaultdict(list)

    for child, parent in dependencies:
        graph[parent].append(child)
        graph[child].extend([])
        in_degree[parent] += 0
        in_degree[child] += 1

    i, compilation_order = 0, [node for node in in_degree if in_degree[node] == 0]
    while i < len(compilation_order):
        for child in graph[compilation_order[i]]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                compilation_order.append(child)
        i += 1

    return compilation_order if len(compilation_order) == len(graph) else []

# Note: expected_free is expected to be sorted in descending order before the order of expected_ordered
# is determined within alien_order. This is for the sake of the test to work.
def alien_order(words):
    if len(words) == 0:
        return ""
    if len(words) == 1:
        return "".join(sorted(words[0]))

    graph, in_count, all_chars = defaultdict(list), defaultdict(int), set()
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        all_chars.update(w1+w2)

        for ch1, ch2 in zip(w1, w2):
            if ch1 != ch2:
                graph[ch1].append(ch2)
                in_count[ch2] += 1
                break
        else:
            if len(w1) > len(w2):
                return ""

    # sorted is not necessary for the algorithm to work and adds unnecessary
    # additional time complexity O(n * log(n)). It is used here only because it
    # allows for the test to work
    # TODO[kat]: Change the test such that sorting is not necessary anymore
    char_order = sorted([ch for ch in all_chars if in_count[ch] == 0])
    i = 0
    while i < len(char_order):
        for ch in graph[char_order[i]]:
            in_count[ch] -= 1
            if in_count[ch] == 0:
                char_order.append(ch)
        i += 1
    
    return "".join(char_order) if len(char_order) == len(all_chars) else ""