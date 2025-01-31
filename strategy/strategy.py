from abc import ABC, abstractmethod
"""
Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a 
separate class that can be execute interchangeably.
"""

class Strategy(ABC):
    """
    Class that defines the interface for the strategy.
    """
    @abstractmethod
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class SubtractStrategy(Strategy):
    def execute(self, a, b):
        return a - b

class MultiplyStrategy(Strategy):
    def execute(self, a, b):
        return a * b

class DivideStrategy(Strategy):
    def execute(self, a, b):
        return a / b

class Context:
    def __init__(self, strategy: Strategy, a: int = 10, b: int = 5):
        self._strategy = strategy
        self.a = a
        self.b = b

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def __call__(self, a, b):
        a = a or self.a
        b = b or self.b
        # overriding the __call__ method, so we can call the context directly
        return self._strategy.execute(a, b)

    def execute_strategy(self, a, b):
        a = a or self.a
        b = b or self.b
        return self._strategy.execute(a, b)


# Usage
# context is initialized with the AddStrategy
context = Context(AddStrategy())
result = context(5, 3)
print(result)  # Output: 8

# context is initialized with the SubtractStrategy
context = Context(SubtractStrategy())
result = context(5, 3)
print(result)  # Output: 2

# context is initialized with the MultiplyStrategy
context = Context(MultiplyStrategy())
result = context(5, 3)
print(result)  # Output: 15
