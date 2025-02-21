# Decorator Design Pattern

The Decorator Design Pattern is a structural pattern that allows behavior to be dynamically added to an object without modifying its original structure. It provides a flexible alternative to subclassing for extending functionality.

## Overview
- **Component**: Defines the common interface for all objects that can have responsibilities added dynamically.
- **Concrete Component**: The base object that can be decorated.
- **Decorator**: Wraps a `Component` and adds additional behavior.
- **Concrete Decorators**: Implement additional behavior while maintaining the `Component` interface.

## Benefits
- **Enhances flexibility**: New functionalities can be added dynamically without altering the existing code.
- **Promotes Open/Closed Principle**: Existing classes remain unchanged while behaviors extend through decorators.
- **Reduces class explosion**: Avoids creating multiple subclasses to handle every possible combination of features.

## Implementation in Python

### Example: Coffee Shop
```python
from abc import ABC, abstractmethod

# Component interface
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

    def description(self):
        return "Simple Coffee"

# Decorator
class CoffeeDecorator(Coffee, ABC):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", Milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ", Sugar"

# Usage
coffee = SimpleCoffee()
print(f"{coffee.description()} costs ${coffee.cost()}")

coffee_with_milk = MilkDecorator(coffee)
print(f"{coffee_with_milk.description()} costs ${coffee_with_milk.cost()}")

coffee_with_milk_sugar = SugarDecorator(coffee_with_milk)
print(f"{coffee_with_milk_sugar.description()} costs ${coffee_with_milk_sugar.cost()}")
```

## Key Features
- **Composition Over Inheritance**: Decorators provide a way to add functionality without modifying base classes.
- **Layered Enhancements**: Multiple decorators can be combined for complex behaviors.
- **Transparency**: The decorated object retains the same interface, making it interchangeable with undecorated objects.

## Conclusion
The Decorator Pattern is useful when objects need additional functionalities dynamically without modifying their structure. It is widely used in GUI frameworks, I/O streams, and logging systems.

---
