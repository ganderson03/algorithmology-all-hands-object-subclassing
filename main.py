import time
import sys

# Define the class hierarchy
class Polygon:
    def area(self):
        return 0  # Default implementation

class Square(Polygon):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2

class BigSquare(Square):
    def __init__(self, side_length, scale_factor=1.5):
        super().__init__(side_length)
        self.scale_factor = scale_factor
    
    def area(self):
        return (self.side_length ** 2) * self.scale_factor

class LittleSquare(Square):
    def __init__(self, side_length, factor=0.5):
        super().__init__(side_length)
        self.factor = factor
    
    def area(self):
        return (self.side_length ** 2) * self.factor


# Function to measure performance of object creation and area calculation
def measure_performance():
    # Define the number of iterations for each type of square
    iterations = 100000

    # Measure time for creating and calculating area of a Square
    start_time = time.time()
    for _ in range(iterations):
        square = Square(5)
        square_area = square.area()
    square_time = time.time() - start_time
    print(f"Square: Time for {iterations} iterations: {square_time:.6f} seconds")
    
    # Measure time for creating and calculating area of a BigSquare
    start_time = time.time()
    for _ in range(iterations):
        big_square = BigSquare(5)
        big_square_area = big_square.area()
    big_square_time = time.time() - start_time
    print(f"BigSquare: Time for {iterations} iterations: {big_square_time:.6f} seconds")
    
    # Measure time for creating and calculating area of a LittleSquare
    start_time = time.time()
    for _ in range(iterations):
        little_square = LittleSquare(5)
        little_square_area = little_square.area()
    little_square_time = time.time() - start_time
    print(f"LittleSquare: Time for {iterations} iterations: {little_square_time:.6f} seconds")

    # Measure memory usage of each object (we calculate memory usage for one object)
    square = Square(5)
    big_square = BigSquare(5)
    little_square = LittleSquare(5)
    print(f"Memory usage of Square object: {sys.getsizeof(square)} bytes")
    print(f"Memory usage of BigSquare object: {sys.getsizeof(big_square)} bytes")
    print(f"Memory usage of LittleSquare object: {sys.getsizeof(little_square)} bytes")

# Running the performance measurement experiment
measure_performance()