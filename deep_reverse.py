def deep_reverse(L):
    for i in L:
        i.reverse()

    L.reverse()


if __name__ == '__main__':
    elements = [
        {'given': [[0, 1, 2], [1, 2, 3]], 'expected': [[3, 2, 1], [2, 1, 0]]},
        {'given': [[0, -1, 2, -3, 4, -5]], 'expected': [[-5, 4, -3, 2, -1, 0]]},
        {'given': [[1], [1, 2, 3]], 'expected': [[3, 2, 1], [1]]},
        {'given': [[], [1, 2, 3]], 'expected': [[3, 2, 1], []]},
        {'given': [[2, -1, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 101, 10, 1, 1, 5, 4, 3]],
         'expected': [[3, 4, 5, 1, 1, 10, 101, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [10, -1, 2]]},
    ]
    for e in elements:
        l = e['given']
        deep_reverse(l)
        assert l == e['expected']