class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        current = self.head
        stack = ""
        while current:
            stack += str(current.data) + "-->"
            current = current.next
        print(stack)

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head.data

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        remove = self.head.next
        self.head.next =
        self.size -= 1
        return remove.data


if __name__ == '__main__':
    stack = Stack()
    print("Stack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. IsEmpty")
    print("4. GetSize")
    print("5. Peek")

    while True:
        n = int(input("Enter yur choice:"))

        match n:
            case 1:
                data = input("Enter a value:")
                stack.push(data)
                stack.__str__()

            case 2:
                print("Removed Element", stack.pop())

            case 3:
                print(stack.is_empty())

            case 4:
                print(stack.get_size())

            case 5:
                print(stack.peek())
