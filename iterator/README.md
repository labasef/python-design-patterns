# Iterator Design Pattern

The Iterator Design Pattern is a behavioral pattern that provides a way to access elements of a collection sequentially without exposing its underlying representation. It separates iteration logic from the collection itself, promoting clean and modular design.

## Overview
- **Iterator Interface**: Defines methods for traversing elements (e.g., `next()`, `has_next()`).
- **Concrete Iterator**: Implements the iterator interface to traverse a specific collection.
- **Collection Interface**: Defines a method to return an iterator.
- **Concrete Collection**: Implements the collection interface and returns an instance of the iterator.

## Benefits
- **Encapsulation**: Hides the internal representation of the collection.
- **Separation of Concerns**: Collection and iteration logic are independent.
- **Supports Multiple Iterations**: Different iterators can traverse the same collection in different ways.

## Implementation in Python

### Example: Custom Iterator for a Number Collection
```python
class NumberIterator:
    def __init__(self, numbers):
        self._numbers = numbers
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index >= len(self._numbers):
            raise StopIteration
        value = self._numbers[self._index]
        self._index += 1
        return value

# Collection class
class NumberCollection:
    def __init__(self, numbers):
        self._numbers = numbers
    
    def __iter__(self):
        return NumberIterator(self._numbers)

# Usage
numbers = NumberCollection([1, 2, 3, 4, 5])
for num in numbers:
    print(num)
```

## Key Features
- **Pythonic Iteration**: Implements `__iter__()` and `__next__()` for built-in iteration support.
- **Custom Iterators**: Allows for defining specific iteration behaviors.
- **Encapsulation**: Keeps iteration logic separate from the collection.

## Conclusion
The Iterator Pattern is essential for handling sequential access to collections in an efficient and maintainable manner. It is widely used in frameworks, collections, and data processing systems.

---
