class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.map = {}  # val -> node
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def length(self):
        return len(self.map)

    def pop(self, key):
        if key in self.map:
            node = self.map[key]
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            del self.map[key]

    def popLeft(self):
        if self.left.next == self.right:
            return None  # List is empty
        key = self.left.next.val
        self.pop(key)
        return key

    def push(self, key):
        node = ListNode(key, self.right.prev, self.right)
        self.map[key] = node
        self.right.prev.next = node
        self.right.prev = node

    def update(self, key):
        self.pop(key)
        self.push(key)

class LFUCache:
    def __init__(self, capacity: int):
        self.map = {}  # key -> val
        self.countMap = defaultdict(int)  # key -> count
        self.freqList = defaultdict(DLL)  # count -> DLL
        self.leastFreq = 0
        self.capacity = capacity

    def counter(self, key):
        count = self.countMap[key]
        self.countMap[key] += 1
        self.freqList[count].pop(key)
        self.freqList[count + 1].push(key)
        if count == self.leastFreq and self.freqList[count].length() == 0:
            self.leastFreq += 1

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.counter(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key not in self.map and len(self.map) == self.capacity:
            res = self.freqList[self.leastFreq].popLeft()
            if res is not None:
                self.map.pop(res)
                self.countMap.pop(res)

        self.map[key] = value
        self.counter(key)
        self.leastFreq = min(self.leastFreq, self.countMap[key])