class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None


class LRUCache:
    '''
    map -> key: node

    linked list -> store key
    - use linked list to move items from middle to end
    - def put_to_end

    node -> key, value

    can create custom reusable set node to end function
    '''

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def add_to_tail(self, node: Node) -> None:
        old_tail = self.tail.prev

        old_tail.next = node
        node.prev = old_tail

        node.next = self.tail
        self.tail.prev = node


    def remove_node(self, node: Node) -> None:
        left = node.prev
        right = node.next

        left.next = right
        right.prev = left


    # def remove_head(self) -> None:
    #     old_head = self.head.prev
    #     new_head = old_head.prev

    #     new_head.next = self.head
    #     self.head.prev = new_head


    def get(self, key: int) -> int:
        '''
        check from map 
        -> if dont exist return -1
        -> if exist -> get node -> get value -> move node to tail
        '''
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove_node(node)
        self.add_to_tail(node)

        return node.val

        
    def put(self, key: int, value: int) -> None:
        '''
        - if key exist in map -> go to node -> update val -> move to tail
        - if key dont exist in map
            -> create new node -> create new map item
            -> enforce size -> delete head -> delete hash map item
        '''
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.remove_node(node)
            self.add_to_tail(node)

            return
        
        # key doesn't exist
        node = Node(key, value)
        self.add_to_tail(node)
        self.cache[key] = node

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove_node(lru)
            del self.cache[lru.key]



        
