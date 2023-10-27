"""
Code illustrating the Single Responsiblity Principle.

SRP: A class should have only one reason to change.
"""

class Model:
    def __init__(self):
        self.name = "Model"
    

class Viewer:
    def __init__(self):
        self.name = "Viewer"

class Controller:
    def __init__(self):
        self.name = "Controller"

    def take_user_input(input):
        apply_user_input()
