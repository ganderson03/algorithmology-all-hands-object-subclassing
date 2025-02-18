import time
import sys

# Base class
class Shape:
    def area(self):
        return 0  # Default implementation

# Level 1: Square, Rectangle, Circle, Triangle, Pentagon, Hexagon, Heptagon, Octagon
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Pentagon(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return (5 / 4) * (self.side_length ** 2) / (3.14159 / 5)

class Hexagon(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return (3 * 3**0.5 / 2) * self.side_length ** 2

class Heptagon(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return (7 / 4) * (self.side_length ** 2) / (3.14159 / 7)

class Octagon(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return 2 * (1 + 2**0.5) * self.side_length ** 2

# Level 2: Square2, Rectangle2, Circle2, Triangle2, Pentagon2, Hexagon2, Heptagon2, Octagon2
class Square2(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Rectangle2(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle2(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

class Triangle2(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Pentagon2(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return (5 / 4) * (self.side_length ** 2) / (3.14159 / 5)

class Hexagon2(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return (3 * 3**0.5 / 2) * self.side_length ** 2

class Heptagon2(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return (7 / 4) * (self.side_length ** 2) / (3.14159 / 7)

class Octagon2(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return 2 * (1 + 2**0.5) * self.side_length ** 2

# Function to measure performance
def measure_performance():
    iterations = 100000

    shapes = [
        (Square(5), "Square (Level 1)"),
        (Rectangle(5, 10), "Rectangle (Level 1)"),
        (Circle(5), "Circle (Level 1)"),
        (Triangle(5, 10), "Triangle (Level 1)"),
        (Pentagon(5), "Pentagon (Level 1)"),
        (Hexagon(5), "Hexagon (Level 1)"),
        (Heptagon(5), "Heptagon (Level 1)"),
        (Octagon(5), "Octagon (Level 1)"),
        
        (Square2(5), "Square (Level 2)"),
        (Rectangle2(5, 10), "Rectangle (Level 2)"),
        (Circle2(5), "Circle (Level 2)"),
        (Triangle2(5, 10), "Triangle (Level 2)"),
        (Pentagon2(5), "Pentagon (Level 2)"),
        (Hexagon2(5), "Hexagon (Level 2)"),
        (Heptagon2(5), "Heptagon (Level 2)"),
        (Octagon2(5), "Octagon (Level 2)"),
    ]

    for shape, name in shapes:
        start_time = time.time()
        for _ in range(iterations):
            _ = shape.area()
        elapsed_time = time.time() - start_time
        print(f"{name}: Time for {iterations} iterations: {elapsed_time:.6f} seconds")
        print(f"Memory usage of {name} object: {sys.getsizeof(shape)} bytes")

# Running the performance measurement experiment
measure_performance()
