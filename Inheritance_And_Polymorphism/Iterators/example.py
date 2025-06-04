# Iterators in Python
# Iterators are objects that allow you to traverse through all the elements in a collection, such as lists or tuples. 
# An iterator is an object that implements the iterator protocol, which consists of the methods `__iter__()` and `__next__()`.

## Overview of Iterators
### Creating an Iterator:
# To create an iterator in Python, you need to implement the `__iter__()` and `__next__()` methods.

class MyIterator:
    def __init__(self, start : int, end : int) -> None:
        self.current : int = start
        self.end : int = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


### Using an Iterator
# You can use an iterator in a `for` loop or manually call the `__next__()` method using the `next()` function.
iterator = MyIterator(1, 5)

for num in iterator:
    print(num)  # Output: 1 2 3 4

# Or manually
iterator = MyIterator(1, 5)
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  # Output: 4
