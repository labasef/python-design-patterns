# Composite Design Pattern

The Composite Design Pattern is a structural pattern used to treat individual objects and compositions of objects uniformly. It enables building a tree structure where both individual and composite objects can be handled through a common interface.

## Overview
- **Component**: Defines the common interface for all objects (leaf and composite).
- **Leaf**: Represents individual objects that do not contain other objects.
- **Composite**: Represents a container that holds multiple components, including other composites.

## Benefits
- **Simplifies client code**: Clients can treat individual objects and groups of objects the same way.
- **Promotes a hierarchical structure**: Useful for tree-like structures (e.g., file systems, UI components).
- **Encourages scalability**: New component types can be easily added without modifying existing code.

## Implementation in Python

### Example: File System Hierarchy
```python
from abc import ABC, abstractmethod

# Component interface
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# Leaf node
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print("  " * indent + f"File: {self.name}")

# Composite node
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def display(self, indent=0):
        print("  " * indent + f"Directory: {self.name}")
        for child in self.children:
            child.display(indent + 1)

# Usage
root = Directory("root")
folder1 = Directory("folder1")
folder2 = Directory("folder2")
file1 = File("file1.txt")
file2 = File("file2.txt")

folder1.add(file1)
folder2.add(file2)
root.add(folder1)
root.add(folder2)

root.display()
```

## Key Features
- **Unified Interface**: `FileSystemComponent` provides a common interface for `File` and `Directory`.
- **Tree Structure**: `Directory` can contain both `File` and other `Directory` objects.
- **Recursive Operation**: The `display()` method works recursively to print the entire hierarchy.

## Conclusion
The Composite Pattern is ideal for representing tree structures where individual and composite objects should be treated uniformly. It is widely used in graphical user interfaces, document structures, and hierarchical data models.

---

