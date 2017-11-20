
def iterate_with_for():
    items = [1, 2, 3, 4, 5]
    for item in items:
        print(item)


def iterate_without_for():
    items = [1, 2, 3, 4, 5]
    try:
        iterator = iter(items)
        while True:
            item = next(iterator)
            print(item)
    except StopIteration:
        pass


print('Iterating with a for loop...')
iterate_with_for()

print('\nIterating without a for loop...')
iterate_without_for()
