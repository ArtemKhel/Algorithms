


// 95% этого кода было сгенерировано из .py при помощи RapydScript



function ՐՏ_with__name__(fn, name) {
    fn.__name__ = name;
    return fn
}

function enumerate(item) {
    var arr, iter, i;
    arr = [];
    iter = ՐՏ_Iterable(item);
    for (i = 0; i < iter.length; i++) {
            arr[arr.length] = [i, item[i]]
    }
    return arr  
}

function ՐՏ_extends(child, parent) {
    child.prototype = Object.create(parent.prototype);
    child.prototype.__base__ = parent;
    child.prototype.constructor = child
}

function ՐՏ_in(val, arr) {
    if (typeof arr.indexOf === "function") {
        return arr.indexOf(val) !== -1
    } else if (typeof arr.has === "function") {
        return arr.has(val)
    }
    return arr.hasOwnProperty(val)
}

function ՐՏ_Iterable(iterable) {
    var tmp;
    if (iterable.constructor === [].constructor || iterable.constructor === "".constructor || (tmp = Array.prototype.slice.call(iterable)).length) {
        return tmp || iterable
    }
    if (Set && iterable.constructor === Set) {
        return Array.from(iterable)
    }
    return Object.keys(iterable)
}

function len(obj) {
    var tmp;
    if (obj.constructor === [].constructor || obj.constructor === "".constructor || (tmp = Array.prototype.slice.call(obj)).length) {
        return (tmp || obj).length
    }
    if (Set && obj.constructor === Set) {
        return obj.size
    }
    return Object.keys(obj).length
}

function range(start, stop, step) {
    var length, idx, range;
    if (arguments.length <= 1) {
        stop = start || 0;
        start = 0
    }
    step = arguments[2] || 1;
    length = Math.max(Math.ceil((stop - start) / step), 0);
    idx = 0;
    range = new Array(length);
    while (idx < length) {
        range[idx++] = start;
        start += step
    }
    return range
}

function ՐՏ_eq(a, b) {
    ;
    var ՐՏitr5, ՐՏidx5;
    var i;
    if (a === b) {
        return true
    }
    if (a === void 0 || b === void 0 || a === null || b === null) {
        return false
    }
    if (a.constructor !== b.constructor) {
        return false
    }
    if (Array.isArray(a)) {
        if (a.length !== b.length) {
            return false
        }
        for (i = 0; i < a.length; i++) {
            if (!ՐՏ_eq(a[i], b[i])) {
                return false
            }
        }
        return true
    } else if (a.constructor === Object) {
        if (Object.keys(a).length !== Object.keys(b).length) {
            return false
        }
        ՐՏitr5 = ՐՏ_Iterable(a);
        for (ՐՏidx5 = 0; ՐՏidx5 < ՐՏitr5.length; ՐՏidx5++) {
            i = ՐՏitr5[ՐՏidx5];
            if (!ՐՏ_eq(a[i], b[i])) {
                return false
            }
        }
        return true
    } else if (Set && a.constructor === Set || Map && a.constructor === Map) {
        if (a.size !== b.size) {
            return false
        }
        for (i of a) {
            if (!b.has(i)) {
                return false
            }
        }
        return true
    } else if (a.constructor === Date) {
        return a.getTime() === b.getTime()
    } else if (typeof a.__eq__ === "function") {
        return a.__eq__(b)
    }
    return false
}

var __name__ = "__main__";
class Vertex {
    constructor(char = "", parent = null) {
        var self = this;
        self.char = char;
        self.final = false;
        self.children = {};
        self.parent = parent;
        self.suff_link = null;
        if (self.parent) {
            self.deep = parent.deep + 1
        } else {
            self.deep = -1
        }
    }
}
class Aho_Corasic {
    constructor(patterns) {
        
        
        var ՐՏitr1, ՐՏidx1;
        var self = this;
        var pattern;
        self.trie = new Vertex;
        self.trie.suff_link = self.trie;
        ՐՏitr1 = ՐՏ_Iterable(patterns);
        for (ՐՏidx1 = 0; ՐՏidx1 < ՐՏitr1.length; ՐՏidx1++) {
            pattern = ՐՏitr1[ՐՏidx1];
            self.add_pattern(pattern.toLowerCase())
        }
    }
    add_pattern(pattern) {
        ;
        var ՐՏitr2, ՐՏidx2;
        var self = this;
        var vertex, char;
        vertex = self.trie;
        ՐՏitr2 = ՐՏ_Iterable(pattern);
        for (ՐՏidx2 = 0; ՐՏidx2 < ՐՏitr2.length; ՐՏidx2++) {
            char = ՐՏitr2[ՐՏidx2];
            if (ՐՏ_in(char, vertex.children)) {
                vertex = vertex.children[char]
            } else {
                vertex.children[char] = new Vertex(char, vertex);
                vertex = vertex.children[char]
            }
        }
        vertex.final = true
    }
    suffix_link (vertex) {
        var ՐՏ_1, ՐՏ_2, ՐՏ_3, ՐՏ_4, ՐՏ_5;
        var self = this;
        if (((ՐՏ_1 = vertex.suff_link) === (ՐՏ_2 = null) || typeof ՐՏ_1 === "object" && ՐՏ_eq(ՐՏ_1, ՐՏ_2))) {
            if ((vertex !== (ՐՏ_3 = self.trie) && (typeof vertex !== "object" || !ՐՏ_eq(vertex, ՐՏ_3))) || ((ՐՏ_4 = vertex.parent) !== (ՐՏ_5 = self.trie) && (typeof ՐՏ_4 !== "object" || !ՐՏ_eq(ՐՏ_4, ՐՏ_5)))) {
                vertex.suff_link = self.trie;
            } else {
                vertex.suff_link = self.transition(self.suffix_link(vertex.parent), vertex.char);
            }
        }
        return vertex.suff_link;
    }
    transition (vertex, char) {
        var ՐՏ_6;
        var self = this;
        if (char in vertex.children) {
            vertex = vertex.children[char];
        } else {
            if ((vertex !== (ՐՏ_6 = self.trie) && (typeof vertex !== "object" || !ՐՏ_eq(vertex, ՐՏ_6)))) {
                vertex.children[char] = self.transition(self.suffix_link(vertex), char);
                vertex = vertex.children[char];
            }
        }
        return vertex;
    }
    
    // * find(string) {
    //     console.log(123)
    //     var ՐՏitr3, ՐՏidx3;
    //     var self = this;
    //     var vertex, pos, char;
    //     vertex = self.trie;
    //     ՐՏitr3 = ՐՏ_Iterable(enumerate(string));
    //     for (ՐՏidx3 = 0; ՐՏidx3 < ՐՏitr3.length; ՐՏidx3++) {
    //         [pos, char] = ՐՏitr3[ՐՏidx3];
    //         vertex = self.transition(vertex, char);
    //         if (vertex.final) {
    //             yield pos - vertex.deep
    //         }
    //     }
    // }
    // replace(string) {
    //     var ՐՏitr4, ՐՏidx4;
    //     var self = this;
    //     var newline, entry, i;
    //     newline = string;
    //     self.find(string)
    //     ՐՏitr4 = ՐՏ_Iterable(self.find(string.toLowerCase()));
    //     for (ՐՏidx4 = 0; ՐՏidx4 < ՐՏitr4.length; ՐՏidx4++) {
    //         entry = ՐՏitr4[ՐՏidx4];
    //         for (i = entry; i < len(string); i++) {
    //             if (string[i].isspace()) {
    //                 break
    //             }
    //         }
    //         newline = "".join([newline.slice(0, entry), "█".repeat(i - entry), newline.slice(i)])
    //     }
    //     return newline
    // }
    find (string) {
        var ՐՏitr3, ՐՏidx3;
        var self = this;
        var vertex, ret, pos, char;
        vertex = self.trie;
        ret = [];
        ՐՏitr3 = ՐՏ_Iterable(enumerate(string));
        for (ՐՏidx3 = 0; ՐՏidx3 < ՐՏitr3.length; ՐՏidx3++) {
            [pos, char] = ՐՏitr3[ՐՏidx3];
            vertex = self.transition(vertex, char);
            if (vertex.final) {
                ret.push(pos - vertex.deep);
            }
        }
        return ret
    }
    replace (string) {
        var ՐՏitr4, ՐՏidx4;
        var self = this;
        var newline, entries, entry, i, j;
        newline = string;
        ՐՏitr4 = ՐՏ_Iterable(self.find(string.toLowerCase()));
        for (ՐՏidx4 = 0; ՐՏidx4 < ՐՏitr4.length; ՐՏidx4++) {
            entry = ՐՏitr4[ՐՏidx4];
            for (i = entry; i < len(string); i++) {
                if (' \s\f\n\r\t\v,.'.includes(string[i])) {
                    break;
                }
            }
            for (j = entry; j > 0; j--) {
            if (' \s\f\n\r\t\v'.includes(string[j])) {
                break;
            }
        }
            newline = [newline.slice(0, j+1), "█".repeat(i - j), newline.slice(i)].join('');
        }
        return newline;
    }
}
