from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None

        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        elif len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        elif len(self.storage) == self.capacity:
            if self.current.next:
                self.current.value = item
                self.current = self.current.next
            else:
                self.current.value = item
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # start at beginning of list
        node = self.storage.head
        while(node):
            list_buffer_contents.append(node.value)
            node = node.next
        return list_buffer_contents




# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass