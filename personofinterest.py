class PersonOfInterest:
    def __init__(self, name: str, str_values: dict):
        """Object to hold name and DNA STR values."""
        self.name = name
        self.str_values = str_values

    def greet(self):
        print("Hello, my name is " + self.name + ". My values are:")
        print(self.str_values)

