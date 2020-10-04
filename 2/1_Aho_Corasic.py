

class Vertex:
    
    def __init__(self, char='', parent=None):
        self.char = char
        self.final = False
        self.children = {}
        self.parent = parent
        self.suff_link = None
        self.deep = parent.deep + 1 if self.parent else -1


class Aho_Corasic:
    
    def __init__(self, patterns):
        self.trie = Vertex()
        self.trie.suff_link = self.trie
        
        for pattern in patterns:
            self.add_pattern(pattern)


    def add_pattern(self, pattern):
        vertex = self.trie
        for char in pattern:
            if char in vertex.children:
                vertex = vertex.children[char]
            else:
                vertex.children[char] = Vertex(char, vertex)
                vertex = vertex.children[char]
        vertex.final = True


    def suffix_link(self, vertex):
        if vertex.suff_link == None:
            if (vertex is self.trie) or (vertex.parent is self.trie):
                vertex.suff_link = self.trie
            else:
                vertex.suff_link = self.transition(self.suffix_link(vertex.parent), vertex.char)
        return vertex.suff_link


    def transition(self, vertex, char):
        try:
            vertex = vertex.children[char]
        except KeyError:
            if vertex != self.trie:
                vertex.children[char] = self.transition(self.suffix_link(vertex), char)
                vertex = vertex.children[char]
        return vertex
    
    
    def find(self, string):
        vertex = self.trie
        for pos, char in enumerate(string):
            vertex = self.transition(vertex, char)
            if vertex.final:
                yield pos - vertex.deep, vertex.deep


if __name__ == '__main__':
    with open('./1_blacklist.txt') as f:
        filter = Aho_Corasic((line.lower().strip() for line in f))
    
    with open('./1_source.txt') as source, open('./1_censored.txt', 'w') as censored:
        for line in source:
            newline = line.strip()
            for entry, len_ in filter.find(line.lower()):
                for i in range(entry + len_, len(line)):
                    if line[i].isspace():
                        break
                newline = "".join((newline[:entry], "█" * (i - entry), newline[i:]))
            print(newline, file=censored)
