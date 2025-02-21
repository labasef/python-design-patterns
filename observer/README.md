# Observer Design Pattern

The Observer Design Pattern is a behavioral pattern that defines a one-to-many dependency between objects, so that when one object (subject) changes state, all its dependents (observers) are notified and updated automatically. This promotes a decoupled and flexible design.

## Overview
- **Subject Interface**: Maintains a list of observers and provides methods to attach, detach, and notify them.
- **Concrete Subject**: Implements the subject interface and notifies observers of state changes.
- **Observer Interface**: Defines an update method that is called when the subject changes.
- **Concrete Observers**: Implement the observer interface and respond to updates.

## Benefits
- **Decoupling**: Subjects and observers interact through an abstract interface, making the system more maintainable.
- **Scalability**: Multiple observers can be dynamically added or removed without modifying the subject.
- **Event-driven Programming**: Ideal for implementing event handling systems.

## Implementation in Python

### Example: Weather Station Notifier
```python
from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

# Concrete Observer
class Display(Observer):
    def __init__(self, name):
        self._name = name
    
    def update(self, temperature):
        print(f"{self._name} Display: Temperature updated to {temperature}°C")

# Subject Interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass
    
    @abstractmethod
    def detach(self, observer):
        pass
    
    @abstractmethod
    def notify(self):
        pass

# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify()
    
    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

# Usage
weather_station = WeatherStation()
display1 = Display("Main")
display2 = Display("Secondary")

weather_station.attach(display1)
weather_station.attach(display2)

weather_station.set_temperature(25)
weather_station.set_temperature(30)
```

## Key Features
- **Decoupled Communication**: Observers and subjects are loosely coupled.
- **Automatic Notifications**: Observers are updated automatically when the subject changes state.
- **Dynamic Attach/Detach**: Observers can be added or removed at runtime.

## Conclusion
The Observer Pattern is widely used in event-driven applications, UI frameworks, and real-time data monitoring systems. It enables efficient state change propagation while maintaining a modular and scalable design.

---
