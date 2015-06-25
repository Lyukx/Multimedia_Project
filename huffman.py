#-*-coding:utf-8-*-
import operator

# enumeration for type of node
class NodeType:
    INTERNAL = 0
    LEAF = 1

class Node:
    def __init__(self, node_type):
        self.node_type = node_type
        self.char = ''
        self.value = 0
        self.left = None
        self.right = None

    def __le__(self, node):
        if self.value <= node.value:
            return True
        else:
            return False

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.left != None:
            print self.left
        if self.right != None:
            print self.right
        return self.char + ":" + str(self.value)

    def __contains__(self, ch):
        return self.char == ch

    def update_char(self, ch):
        self.char = ch

    def update_value(self, value):
        self.value = value


def traversal(root, sequence, coding):
    if root == None:
        return 

    if root.node_type == NodeType.LEAF:
        if len(sequence) == 0:
            sequence.append('0')
        coding[root.char] = sequence

    else:
        if root.left != None:
            s = sequence[:]
            s.append('0')
            traversal(root.left, s, coding)
        if root.right != None:
            s = sequence[:]
            s.append('1')
            traversal(root.right, s, coding)

def huffman_encode(src, coding):
    # get value of each char
    value = {}
    for char in src:
        if char in value:
            value[char] += 1
        else:
            value[char] = 1
    value = (sorted(value.items(), key=operator.itemgetter(1)))

    # get nodes
    root = []
    for key, v in value:
        node = Node(NodeType.LEAF)
        node.update_char(key)
        node.update_value(v)
        root.append(node)

    # generate huffman tree, root is root[0]
    while len(root) != 1:
        node = Node(NodeType.INTERNAL)
        node.update_value(root[0].value + root[1].value)
        node.left = root[0]
        node.right = root[1]
        root.pop(0)
        root.pop(0)
        
        if len(root) == 0:
            root.append(node)
        else:
            for i in range(0, len(root)):
                if node.value < root[i].value:
                    root.insert(i, node)
                    break
            else:
                root.append(node)

    # traversal the tree to get encoding
    sequence = []
    traversal(root[0], sequence, coding)

    result = []
    for char in src:
        result.extend(coding[char])

    return result

def huffman_decode(src, coding):
    # generate a huffman tree by coding table
    root = Node(NodeType.INTERNAL)
    for k in coding:
        temp = root
        for item in coding[k]:
            if item == '0':
                if temp.left == None:
                    temp.left = Node(NodeType.INTERNAL)
                temp = temp.left
            if item == '1':
                if temp.right == None:
                    temp.right = Node(NodeType.INTERNAL)
                temp = temp.right
        temp.node_type = NodeType.LEAF
        temp.char = k

    # decoding by tree
    result = []
    temp = root
    for c in src:
        if c == '0':
            if temp.left == None:
                raise Exception("Unexpected token")
            temp = temp.left
        if c == '1':
            if temp.left == None:
                raise Exception("Unexpected token")
            temp = temp.right
        if temp.node_type == NodeType.LEAF:
            result.append(temp.char)
            temp = root

    return result

if __name__ == "__main__":
    s = raw_input()
    coding = {}
    result = huffman_encode(s, coding)
    print "Encoding result: "
    print ''.join(result)
    print "Encoding table: "
    print coding 
    
    result = huffman_decode(result, coding)
    print "Decoding result" 
    print ''.join(result)
