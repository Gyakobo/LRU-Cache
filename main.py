class Node:
    def __init__(self, key=None, value=None):
        key     = None
        val     = None
        left    = None
        right   = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {int: Node} # Points to all the Nodes

        self.head = Node()
        self.tail = Node()

        self.head.right = self.tail
        self.tail.left = self.head

    def get(self, key: int) -> int:
        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            newNode = Node(key, value)

            self.hashmap[key] = newNode
            boiler = self.head.right
            self.head.right = newNode
            boiler.left = newNode

        else:
            curNode = self.hashmap[key]
            curNode.val = value

            boilerLeft = curNode.left
            boilerRight = curNode.right
            self.head.right = curNode
            boilerLeft.right = boilerRight
            boilerRight.left = boilerLeft


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)