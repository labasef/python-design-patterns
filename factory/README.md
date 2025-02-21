# Factory Design Pattern

The Factory Design Pattern is a creational pattern that provides an interface for creating objects in a superclass while allowing subclasses to alter the type of objects that will be created. This promotes loose coupling between client code and concrete classes.

## Overview
- **Factory Method**: Defines an interface for creating an object but allows subclasses to alter the object type.
- **Concrete Products**: Specific implementations of the product interface.
- **Factory Class**: Encapsulates object creation logic and returns instances of concrete products.

## Benefits
- **Encapsulation of Object Creation**: Hides object creation logic from the client.
- **Supports Open/Closed Principle**: New product types can be introduced without modifying existing code.
- **Loose Coupling**: The client depends on an abstract interface rather than concrete implementations.

## Implementation in Python

### Example: Shape Factory
```python
from abc import ABC, abstractmethod

# Product Interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete Products
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

# Factory Class
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Square":
            return Square()
        else:
            raise ValueError("Unknown shape type")

# Usage
shape1 = ShapeFactory.get_shape("Circle")
print(shape1.draw())

shape2 = ShapeFactory.get_shape("Square")
print(shape2.draw())
```

## Key Features
- **Static Factory Method**: Clients call a single method to create objects, avoiding direct instantiation.
- **Flexible Object Creation**: New product types can be introduced with minimal modifications.
- **Encapsulation**: The factory class centralizes the instantiation logic.

## Conclusion
The Factory Pattern is useful when object creation logic is complex or should be centralized. It is widely used in frameworks, dependency injection, and database connection handling.

---
