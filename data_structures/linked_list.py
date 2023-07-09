class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, data):
        self.head = Node(value=data[0])
        curr = self.head

        for i in range(1, len(data)):
            n = Node(value=data[i])
            curr.next = n
            curr = curr.next

        return self.head

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    def insert_end(self, value):
        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = Node(value=value)

    def insert_start(self, value):
        curr = Node(value=value, next=self.head)
        self.head = curr


    def insert_after_node(self, pos, val):
        curr = self.head
        while curr:
            if curr.val == pos:
                n = Node(value=val)
                n.next = curr.next
                curr.next = n
                break

            curr = curr.next

    def search_element(self, ele):
        curr = self.head
        while curr:
            if curr.val == ele:
                return True
        return False

    def length_of_list(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        return count

    def remove(self, val):
        curr = self.head
        while curr.next.val != val:
            curr = curr.next

        curr.next = curr.next.next

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        self.head = prev

class Node:
    def __init__(self, next=None, value=None):
        self.next = next
        self.val = value

if __name__ == '__main__':
    linked_list_obj = LinkedList()
    c = linked_list_obj.create([1, 2, 3, 4, 5, 6, 7])
    linked_list_obj.insert_end(8)
    linked_list_obj.insert_start(0)
    linked_list_obj.insert_after_node(5, 10)
    linked_list_obj.traverse()
    linked_list_obj.remove(10)
    linked_list_obj.reverse()
    linked_list_obj.traverse()