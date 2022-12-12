import types
import copy


def flat_generator(list_of_list):
    copy_list_of_list = copy.deepcopy(list_of_list)
    items = []
    item = []
    while True:
        if not copy_list_of_list and not items:
            break
        if not items:
            items = copy_list_of_list.pop(0)
        if not isinstance(items,list):
            yield items
            items = []
        else:
            item = items.pop(0)
            if not isinstance(item,list):
                yield item
            else:
                counter = 0
                for i in item:
                    items.insert(counter,i)
                    counter += 1

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
    print('успешно')