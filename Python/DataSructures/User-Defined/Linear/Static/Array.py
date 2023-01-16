class Array:
    def __init__(self):
        # Size of dynamic array
        self.size = 0
        # Maximum of capacity of dynamic array
        self.capacity = 1
        self.array = self._create_array(self.capacity)

    def __len__(self):
        """
        Length of array
        :return: int
        """
        return self.size

    def __get_item__(self, index):
        """
        Returns the element of a given index
        :param index:
        :return:
        """
        if not 0 <= index < self.size:
            raise IndexError('Given index: {0} is larger than array size {1}'.format(index, self.size))
        return self.array[index]

    def _resize(self, new_capacity):
        """
        Add a new element to the end of the array
        :param new_capacity:
        :return:
        """
        new_array = self._create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def _create_array(self, length):
        """
        Create the array with given size
        :param length: int
        :return:
        """
        return [None] * length


if __name__ == '__main__':
    array = Array()
    print(array)
