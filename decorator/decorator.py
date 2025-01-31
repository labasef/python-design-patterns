from abc import ABC, abstractmethod
"""
Decorator is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside 
special wrapper objects that contain the new behaviors.
"""
class Component(ABC):
    @abstractmethod
    def __call__(self) -> str:
        pass

    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    def __call__(self) -> str:
        return "ConcreteComponent"

    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    def __call__(self) -> str :
        return self._component()

    def operation(self) -> str:
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def __call__(self):
        return f"ConcreteDecoratorA({self._component()})"

    def operation(self) -> str:
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    def __call__(self):
        return f"ConcreteDecoratorB({self._component()})"

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self._component.operation()})"

# Usage
simple = ConcreteComponent()
print(simple.operation())  # Output: ConcreteComponent

decorator1 = ConcreteDecoratorA(simple)
decorator2 = ConcreteDecoratorB(decorator1)
print(decorator2.operation())  # Output: ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))

# using the __call__ method
print(decorator2())  # Output: ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))