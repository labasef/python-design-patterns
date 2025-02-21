# Template Method Design Pattern in Python

## Introduction

The **Template Method Pattern** is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but allows subclasses to implement specific steps of the algorithm. The idea is to allow the invariant parts of the algorithm to be implemented in the superclass while the variable parts are deferred to subclasses. This helps to avoid code duplication by reusing common steps in the algorithm while providing flexibility for customization.

## Use Case

The Template Method Pattern is useful when you have a common algorithm with certain steps that are the same across multiple classes, but some steps of the algorithm need to be customized or extended. The pattern defines the common algorithm structure in a method and lets subclasses define the detailed behavior.

## Example in Python

Below is an example demonstrating how to implement the Template Method pattern in Python.

### Step 1: Define the Abstract Base Class

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process(self):
        # Common steps
        self.load_data()
        self.process_data()
        self.save_data()
    
    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass
```

The `DataProcessor` class defines the "template method" `process`, which calls three steps of the algorithm: `load_data`, `process_data`, and `save_data`. These steps are abstract methods that must be implemented by subclasses.

### Step 2: Create Concrete Classes
```python
class CSVDataProcessor(DataProcessor):
    def load_data(self):
        print("Loading CSV data...")
    
    def process_data(self):
        print("Processing CSV data...")
    
    def save_data(self):
        print("Saving CSV data...")

class JSONDataProcessor(DataProcessor):
    def load_data(self):
        print("Loading JSON data...")
    
    def process_data(self):
        print("Processing JSON data...")
    
    def save_data(self):
        print("Saving JSON data...")
```

Here, `CSVDataProcessor` and `JSONDataProcessor` are concrete implementations of `DataProcessor`. They each provide their specific implementations of the `load_data`, `process_data`, and `save_data` methods.
### Step 3: Use the Template Method Pattern
```python
if __name__ == "__main__":
    # Using the CSV data processor
    csv_processor = CSVDataProcessor()
    csv_processor.process()
    
    print("\n----\n")
    
    # Using the JSON data processor
    json_processor = JSONDataProcessor()
    json_processor.process()
```
The client code uses the `process` method from the `DataProcessor` class, which automatically calls the template method that includes common steps. The specific steps (like loading, processing, and saving data) are delegated to the subclasses, allowing flexibility in their implementation.

#### Output:
```plaintext
Loading CSV data...
Processing CSV data...
Saving CSV data...

----
Loading JSON data...
Processing JSON data...
Saving JSON data...
```
### Advantages of the Template Method Pattern

**Code Reusability**: Common algorithmic steps can be reused in the base class, while specific steps are defined in the subclasses.
**Flexibility**: Allows the customization of certain steps of the algorithm in subclasses, enabling more specific behaviors.
**Avoids Duplication**: Reduces the need for code duplication in subclasses by moving shared logic to a common place.
**Control Over the Algorithm**: The base class defines the overall structure and flow of the algorithm, while subclasses handle the specific details.

### Disadvantages of the Template Method Pattern

**Inflexibility in Method Order**: The algorithm structure defined in the base class cannot be changed in subclasses. This could be limiting in some cases if the order of steps needs to be modified.
**Inheritance Overhead**: It relies heavily on inheritance, which may not always be suitable depending on the application’s design.

## Conclusion

The Template Method Pattern is a useful design pattern when you have an algorithm with invariant parts that should be shared across different subclasses, but you want to allow subclasses to define certain custom steps of the algorithm. It provides a way to control the structure of an algorithm while giving flexibility for customization.