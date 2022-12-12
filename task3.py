import copy

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = copy.deepcopy(list_of_list)
        

    def __iter__(self):
        self.items = self.list_of_list.pop(0)
        self.item = []
        return self
    
    def __next__(self):
        while True: 
            if not self.list_of_list and not self.items:
                raise StopIteration
            if not self.items:
                self.items = self.list_of_list.pop(0)
            
            if not isinstance(self.items,list):
                self.item = self.items
                self.items = []
                return self.item
            else:
                self.item = self.items.pop(0)
                if not isinstance(self.item,list):
                    return self.item
                else:
                    counter = 0
                    for i in self.item:
                        self.items.insert(counter,i)
                        counter += 1


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()