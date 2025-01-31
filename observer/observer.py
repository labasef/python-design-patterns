from abc import ABC, abstractmethod
"""
Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about 
any events that happen to the object they're observing.
"""

class Subject:
    def __init__(self):
        # List of subscribers. In real life, the list of subscribers can be stored more comprehensively (categorized by event type, etc.).
        self._observers = []

    def attach(self, observer):
        # Attach an observer to the subject.
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        # Detach an observer from the subject.
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        # Notify all observers about an event.
        for observer in self._observers:
            observer.update(self)

class ConcreteSubject(Subject):
    def some_business_logic(self, n):
        print(f"Subject: event {str(n)}")
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class ConcreteObserverA(Observer):
    def update(self, subject):
        if isinstance(subject, Subject):
            print("ConcreteObserverA: Reacted to the event")

class ConcreteObserverB(Observer):
    def update(self, subject):
        if isinstance(subject, Subject):
            print(f"ConcreteObserverB: Reacted to the event")

# Usage
subject = ConcreteSubject()
observer1 = ConcreteObserverA()
observer2 = ConcreteObserverB()

subject.attach(observer1)
subject.attach(observer2)

subject.some_business_logic(10)
# Output:
# ConcreteObserverA: Reacted to the event
# ConcreteObserverB: Reacted to the event
