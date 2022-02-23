"""                      Array          Linked List
Indexing                  O(1)              O(n)
Insert/Delete at first    O(n)              O(1)
Insert/Delete at last     O(1)              O(n)
Insert/Delete at middle   O(n)              O(n)

"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def __print__(self):
        if self.head is None:
            print("Linkedlist is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '->'
            itr = itr.next

        print(llstr)

    def insert_values(self, data_list):
        self.head = None                                #new linkedlist

        for data in data_list:
            self.insert_at_end(data)

    def _get_len(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at_index(self, index):
        if index < 0 or index > self._get_len():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next

        count=0
        itr = self.head
        
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next

    def insert_at_index(self, index, data):
        if index < 0 or index > self._get_len():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begin(data)

        count=0
        itr = self.head
        
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([10,20,30,40,50])
    ll.__print__()
    ll.remove_at_index(1)
    ll.__print__()
    ll.insert_at_index(2, 25)
    ll.__print__()