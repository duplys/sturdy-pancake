"""
Code illustrating inheritance.
"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass  # This method will be overridden in the derived classes


class Dog(Animal):
    def speak(self):
        return f"{self.name} the {self.species} barks"


class Cat(Animal):
    def speak(self):
        return f"{self.name} the {self.species} meows"


# Example usage
dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")

print(dog.speak())  # Output: "Buddy the Dog barks"
print(cat.speak())  # Output: "Whiskers the Cat meows"
