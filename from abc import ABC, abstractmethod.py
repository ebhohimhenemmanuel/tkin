from abc import ABC, abstractmethod

class BaseClass(ABC):
    def display_value(self, value):
        print(f"The value is: {value}")

    @abstractmethod
    def abstract_method(self):
        pass

class SubClass(BaseClass):
    def abstract_method(self):
        print("This is the implementation of the abstract method.")

# Example of usage
if __name__ == "__main__":
    obj = SubClass()
    obj.display_value(10)
    obj.abstract_method()
