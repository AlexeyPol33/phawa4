class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.start = 0
        self.end = len(list_of_list) - 1

    def __iter__(self):
        self.items = self.list_of_list
        self.items_start = 0
        self.items_end = len(self.items)
        if self.items:
            self.items = self.list_of_list[self.start]
        return self

    def __next__(self):
        if self.start == self.end and self.items_start == self.items_end:
            raise StopIteration
        if self.items_start == self.items_end:
            self.start +=1
            self.items = self.list_of_list[self.start]
            self.items_start = 0
            self.items_end = len(self.items)
        item = self.items[self.items_start]
        self.items_start += 1
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    


if __name__ == '__main__':
    test_1()
    print('успешно')