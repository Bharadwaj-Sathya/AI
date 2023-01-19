class Array:
    def __init__(self):
        # Size of dynamic array
        self.size = 0
        # Maximum of capacity of dynamic array
        self.capacity = 1
        self.array = self.__createArray__(self.capacity)

    def __len__(self):
        """
        Length of array
        :return: int
        """
        return self.size

    def __getItem__(self, index):
        """
        Returns the element of a given index
        :param index:
        :return:
        """
        if not 0 <= index < self.size:
            raise IndexError('Given index: {0} is larger than array size {1}'.format(index, self.size))
        return self.array[index]

    def __createArray__(self, length):
        """
        Create the array with given size
        :param length: int
        :return:
        """
        self.array = [None] * length
        return self.array

    def __resize__(self, new_capacity):
        """
        Add a new element to the end of the array
        :param new_capacity:
        :return:
        """
        new_array = self.__createArray__(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def __append__(self, val):

        if self.size == self.capacity:
            self.__resize__(2 * self.capacity)

        self.array[self.capacity] = val
        self.capacity += 1

    def __insertAt__(self, pos, val):

        if pos < 0 or pos > self.size:
            print("Please enter an appropriate index")
            return

        if self.size == self.capacity:
            self.__resize__(2 * self.capacity)

        i = self.capacity - 1
        while i >= pos:
            self.array[i + 1] = self.array[i]
            i -= 1

        self.array[pos - 1] = val
        self.capacity += 1

    def __remove__(self):
        if self.capacity > 0:
            self.array[self.capacity - 1] = None
            self.capacity -= 1

    def __removeAt__(self, pos):

        if pos < 0 or pos > self.size:
            print("Please enter an appropriate index")
            return

        index = pos - 1
        while index < self.capacity - 1:
            self.array[index] = self.array[index + 1]
            index += 1
        self.array[self.capacity] = None
        self.capacity -= 1

    def __printArray__(self):
        for i in range(0, self.capacity-1):
            print(self.array[i],"-->")

if __name__ == '__main__':
    array = Array()
    print("-----------------------------Array-----------------------------")
    print("1. Create Array")
    print("2. Append")
    print("3. Insert At Position")
    print("4. Remove")
    print("5. Remove At Position")
    print("7. Length of S")
    print("8. Traverse Singly Linked List")
    print("9. Search in Singly Linked List")
    print("10. Sort Singly Linked List")
    print("11. Quit")

    while True:
        n = int(input("Enter your choice:").strip())
        # This code runs only in python 3.10 or above versions
        match n:
            case 1:
                length = int(input("Enter a length of an array:"))
                array.__createArray__(length)
            case 2:
                data = input("Enter a value:")
                array.__append__(data)
                array.__printArray__()
            case 3:
                data = input("Enter a value:")
                pos = int(input("Enter a position:"))
                array.__insertAt__(pos, data)
            case 4:
                array.__remove__()
            case 5:
                position = int(input("Enter a position:"))
                array.__removeAt__(position)
            # case 6:
            #     singlyLinkedList.remove_at_end()
            # case 7:
            #     print("Length of Singly Linked List:", singlyLinkedList.length_of_singly_linked_list())
            # case 8:
            #     singlyLinkedList.traversal_singly_linked_list()
            # case 9:
            #     singlyLinkedList.traversal_singly_linked_list()
            #     data = input("Enter a value:")
            #     singlyLinkedList.search_singly_linked_list(data)
            # case 10:
            #     singlyLinkedList.sort_singly_linked_list()
            case 11:
                break
    print("---------------------------------------------------------------")
