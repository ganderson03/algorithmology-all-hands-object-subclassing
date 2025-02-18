import time
import scalene

# Base class
class Shape:
    def area(self):
        return 0  # Default implementation

# Level 1: Square
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Level 2: Rectangle
class Rectangle(Square):
    def __init__(self, width, height):
        super().__init__(width)
        self.height = height

    def area(self):
        return self.side_length * self.height

# Level 3: Circle
class Circle(Rectangle):
    def __init__(self, radius):
        super().__init__(radius, radius)  # Pass same value for width and height
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

# Level 4: Triangle
class Triangle(Circle):
    def __init__(self, base, height):
        super().__init__(base)  # Pass only base as Circle expects one argument
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Level 5: Pentagon
class Pentagon(Triangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)  # Pass two identical values

    def area(self):
        return (5 / 4) * (self.side_length ** 2) / (3.14159 / 5)

# Level 6: Hexagon
class Hexagon(Pentagon):
    def __init__(self, side_length):
        super().__init__(side_length)

    def area(self):
        return (3 * 3**0.5 / 2) * self.side_length ** 2

# Level 7: Heptagon
class Heptagon(Hexagon):
    def __init__(self, side_length):
        super().__init__(side_length)

    def area(self):
        return (7 / 4) * (self.side_length ** 2) / (3.14159 / 7)

# Level 8: Octagon
class Octagon(Heptagon):
    def __init__(self, side_length):
        super().__init__(side_length)

    def area(self):
        return 2 * (1 + 2**0.5) * self.side_length ** 2

# Level 9: DeepSquare (Identical to Square but at the bottom)
class DeepSquare(Octagon):
    def __init__(self, side_length):
        super().__init__(side_length)

    def area(self):
        return self.side_length ** 2  # Same calculation as Square

# Level 10: DeepRectangle (Identical to Rectangle but at the bottom)
class DeepRectangle(DeepSquare):
    def __init__(self, width, height):
        super().__init__(width)
        self.height = height

    def area(self):
        return self.side_length * self.height  # Same calculation as Rectangle

# Function to measure performance
def measure_performance():
    iterations = 1000000

    shapes = [
        (Square(5), "Square (Top)"),
        (Rectangle(5, 10), "Rectangle (Top)"),
        (DeepSquare(5), "Square (Bottom)"),
        (DeepRectangle(5, 10), "Rectangle (Bottom)"),
    ]

    for shape, name in shapes:
        start_time = time.time()
        for _ in range(iterations):
            _ = shape.area()
        elapsed_time = time.time() - start_time

        # Print the results
        print(f"{name}: Time for {iterations} iterations: {elapsed_time:.6f} seconds")

# Running the performance measurement experiment
measure_performance()