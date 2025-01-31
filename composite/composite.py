from abc import ABC, abstractmethod
"""
Composite is a structural design pattern that lets you compose objects into tree structures.
Composite lets clients treat individual objects and compositions of objects uniformly.
"""
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class Child(Component):
    def __call__(self) -> str:
        return "Child"
    def operation(self) -> str:
        return "Child"

class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def __call__(self) -> str:
        results = []
        for child in self._children:
            results.append(child())  # calling the __call__ method
        return f"Composite({', '.join(results)})"

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())  # calling the operation method
        return f"Composite({', '.join(results)})"

# Usage
child1 = Child()
child2 = Child()
composite = Composite()
composite.add(child1)
composite.add(child2)
print(composite.operation())  # using the operation function Output: Composite(Child, Child)
print(composite())  # using the __call__ method Output: Composite(Child, Child
