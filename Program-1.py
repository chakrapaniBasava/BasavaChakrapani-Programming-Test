
class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def calculate(self, operation: str) -> float:
        if operation == "add":
            return self.a + self.b
        elif operation == "subtract":
            return self.a - self.b
        elif operation == "multiply":
            return self.a * self.b
        elif operation == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

# Example usage
a = float(input("Enter a: "))
b = float(input("Enter b: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

calc = Calculator(a, b)
print("Result:", calc.calculate(operation))
