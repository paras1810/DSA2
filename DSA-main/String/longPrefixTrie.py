ALPHABET_SIZE = 26
indexs = 0
class TrieNode:
    def __init__(self):
        self.isLeaf = False
        self.children = [None]*ALPHABET_SIZE

def insert(key, root):
    pcrawl = root
    for i in range(len(key)):
        index = ord(key[i]) - ord('a')
        if pcrawl.children[index] == None:
            pcrawl.children[index] = TrieNode()
        pcrawl = pcrawl.children[index]
    pcrawl.isLeaf = True

def countChild(node):
    count = 0
    for i in range(ALPHABET_SIZE):
        if node.children[i] != None:
            count +=1
            global indexs
            indexs = i
    return count

def constructTrie(arr, n, root):
    for i in range(n):
        insert(arr[i], root)

def walkTrie(root):
    pcrawl = root
    prefix = ""
    while countChild(pcrawl) == 1 and pcrawl.isLeaf == False:
        pcrawl = pcrawl.children[indexs]
        prefix += chr(97+indexs)
    return prefix or -1

def commonPrefix(arr, n, root):
    constructTrie(arr, n, root)
    return walkTrie(root)

if __name__ == '__main__':
    n = 4
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
    root = TrieNode()
    print(commonPrefix(arr,n, root))