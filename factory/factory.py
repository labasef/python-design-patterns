from abc import ABC, abstractmethod

"""
Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, 
but allows subclasses to alter the type of objects that will be created.
"""


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: {product.operation()}"
        return result


class ConcreteCreator1(Creator):
    # inherits from Creator and implements the factory_method
    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    # inherits from Creator and implements the factory_method
    def factory_method(self):
        return ConcreteProduct2()


class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteProduct1(Product):
    def operation(self):
        return "{Result of ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self):
        return "{Result of ConcreteProduct2}"


# Usage
creator1 = ConcreteCreator1()
print(creator1.some_operation())  # Output: Creator: {Result of ConcreteProduct1}
creator2 = ConcreteCreator2()
print(creator2.some_operation())  # Output: Creator: {Result of ConcreteProduct2}
