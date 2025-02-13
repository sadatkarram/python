
# Assignment for Overloading and Overriding

class Shape :
    def calculate_area() :
        return "Unknown shape"
    
class Circle(Shape):
    def __init__(self, r):
        self.r =r
        
    def calculate_area(self, r):
        return 3.14 * r

class Rectangle(Shape):
    def __init__(self, width, height) :
        self.width = width
        self.height = height
    
    def calculate_area(self, width, height):
        return width * height
    

circle_obj = Circle(3)
print(f"Area of Circle with radius({circle_obj.r}) = {circle_obj.calculate_area(circle_obj.r)}")

rect_obj = Rectangle(3,4)
print(f"Area of Rectangle with width({rect_obj.width}) and height({rect_obj.height}) = {rect_obj.calculate_area(rect_obj.width,rect_obj.height)}")

# Area of Circle with radius(3) = 30.959144000000002
# Area of Rectangle with width(3) and height(4) = 81
        