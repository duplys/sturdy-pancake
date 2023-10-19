"""
Code illustrating encapsulation.
"""

class Person:
    def __init__(self, name, age):
        # Private attributes
        self._name = name
        self._age = age

    # Getter methods for accessing private attributes
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    # Setter methods for modifying private attributes
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name

    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 120:
            self._age = age

    # Private method
    def _validate_age(self, age):
        return isinstance(age, int) and 0 <= age <= 120

# Example usage
person = Person("Alice", 30)

# Accessing attributes through getters
print("Name:", person.get_name())
print("Age:", person.get_age())

# Modifying attributes through setters
person.set_name("Bob")
person.set_age(35)

print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())
