"""
The Singleton pattern is a creational design pattern that lets you ensure that a class has only one instance,
while providing a global access point to this instance.
"""


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# Usage
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Output: True
