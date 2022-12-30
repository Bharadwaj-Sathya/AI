class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.traversal_singly_linked_list()

    def insert_at_position(self, data, pos):
        if pos < 0 or pos > self.length_of_singly_linked_list():
            print("Invalid Position")
        elif pos == 1 or pos == 0:
            self.insert_at_beginning(data)
        else:
            count = 1
            index = self.head
            while index:
                if count == pos - 1:
                    node = Node(data)
                    index.next = node
                    break
                index = index.next
                count += 1
            self.traversal_singly_linked_list()

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            pos = self.head
            while pos.next:
                pos = pos.next
            pos.next = node
        self.traversal_singly_linked_list()

    def remove_at_beginning(self):
        if self.head is None:
            print("Singly Linked List is Empty")
        else:
            self.head = self.head.next
            self.traversal_singly_linked_list()

    def remove_at_position(self, pos):
        if pos < 0 or pos > self.length_of_singly_linked_list():
            print("Invalid Position")
        elif pos == 1 or pos == 0:
            self.remove_at_beginning()
        else:
            index = self.head
            count = 1
            while index:
                if count == pos - 1:
                    index.next = index.next.next
                    break
                index = index.next
                count += 1
            self.traversal_singly_linked_list()

    def remove_at_end(self):
        if self.head is None:
            print("Singly Linked List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            index = self.head
            while index.next.next:
                index = index.next
            index.next = None

        self.traversal_singly_linked_list()

    def length_of_singly_linked_list(self):
        count = 0
        pos = self.head
        while pos:
            count += 1
            pos = pos.next
        return count

    def traversal_singly_linked_list(self):
        if self.head is None:
            print("Singly Linked List is Empty")
        else:
            pos = self.head
            lis_str = ''
            while pos:
                lis_str += str(pos.data) + '-->'
                pos = pos.next
            print("Singly Linked List :", lis_str)

    def search_singly_linked_list(self, data):
        index = self.head
        while index is not None:
            if index.data == data:
                print(True)
                break
            index = index.next
        else:
            print(False)

    def sort_singly_linked_list(self):
        if self.head is None:
            print("Singly Linked List is Empty")
        else:
            current_node = self.head
            while current_node is not None:
                next_node = current_node.next
                while next_node is not None:
                    if current_node.data > next_node.data:
                        current_node.data, next_node.data = next_node.data, current_node.data
                    next_node = next_node.next
                current_node = current_node.next
        self.traversal_singly_linked_list()


if __name__ == '__main__':
    singlyLinkedList = LinkedList()
    print("Singly Linked List Operations:")
    print("1. Insert At Beginning")
    print("2. Insert At Position")
    print("3. Insert At End")
    print("4. Remove At Beginning")
    print("5. Remove At Position")
    print("6. Remove At End")
    print("7. Length of Singly Linked List")
    print("8. Traverse Singly Linked List")
    print("9. Search in Singly Linked List")
    print("10. Sort Singly Linked List")
    print("11. Quit")

    while True:
        n = int(input("Enter your choice:").strip())
        match n:
            case 1:
                data = input("Enter a value:")
                singlyLinkedList.insert_at_beginning(data)
            case 2:
                data = input("Enter a value:")
                pos = int(input("Enter a position:"))
                singlyLinkedList.insert_at_position(data, pos)
            case 3:
                data = input("Enter a value:")
                singlyLinkedList.insert_at_end(data)
            case 4:
                singlyLinkedList.remove_at_beginning()
            case 5:
                position = int(input("Enter a position:"))
                singlyLinkedList.remove_at_position(position)
            case 6:
                singlyLinkedList.remove_at_end()
            case 7:
                print("Length of Singly Linked List:", singlyLinkedList.length_of_singly_linked_list())
            case 8:
                singlyLinkedList.traversal_singly_linked_list()
            case 9:
                singlyLinkedList.traversal_singly_linked_list()
                data = input("Enter a value:")
                singlyLinkedList.search_singly_linked_list(data)
            case 10:
                singlyLinkedList.sort_singly_linked_list()
            case 11:
                break
