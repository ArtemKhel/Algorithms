

class Vertex:
    
    def __init__(self, char='', parent=None):
        self.char = char
        self.final = False
        self.children = {}
        self.parent = parent
        self.suff_link = None
        if self.parent:
            self.deep = parent.deep + 1
        else:
            self.deep = -1
        # self.deep = parent.deep + 1 if self.parent else -1


class Aho_Corasic:
    
    def __init__(self, patterns):
        self.trie = Vertex()
        self.trie.suff_link = self.trie
        
        for pattern in patterns:
            self.add_pattern(pattern)
        
        pass


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
            if (vertex != self.trie) or (vertex.parent != self.trie):
                vertex.suff_link = self.trie
            else:
                vertex.suff_link = self.transition(self.suffix_link(vertex.parent), vertex.char)
        return vertex.suff_link


    def transition(self, vertex, char):
        if char in vertex.children.keys():
            vertex = vertex.children[char]
        else:
            if vertex != self.trie:
                vertex.children[char] = self.transition(self.suffix_link(vertex), char)
                vertex = vertex.children[char]
        return vertex
    
    
    def find(self, string):
        vertex = self.trie
        ret = []
        for pos, char in enumerate(string):
            vertex = self.transition(vertex, char)
            if vertex.final:
                ret.appent(pos - vertex.deep)

    
    def replace(self, string):
        newline = string
        string.lower()
        entries = self.find(string)
        for entry in entries:
            for i in range(entry, len(string)):
                if string[i].isspace():
                    break

            # Replace '█' with '█'.repeat(i-entry) in js code
            newline = ''.join((newline[:entry], '█', newline[i:]))
        return newline



