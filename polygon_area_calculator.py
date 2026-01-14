class Rectangle:
    def __init__(self, width, height):
        self.width = width   # ← Sin guión bajo (público)
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, value):  # ← Método tradicional
        self.width = value
        
    def set_height(self, value):  # ← Método tradicional
        self.height = value
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return pow((self.width**2 + self.height**2),0.5)

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        picture = ""
        for i in range(self.height):
            line = ("*" * self.width) + "\n"
            picture += line
        return picture

    def get_amount_inside(self, figure):
        width_result = self.width // figure.width
        height_result = self.height // figure.height
        result = width_result * height_result
        return result
        


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, value):
        self.width = value
        self.height = value

    def set_height(self, value):
        self.width = value
        self.height = value

    def set_side(self, value):
        self.width = value
        self.height = value

rectangle1 = Rectangle(10,5)
print(rectangle1.get_area())
rectangle1.set_height(3)
print(rectangle1.get_perimeter())
print(rectangle1.get_picture())
