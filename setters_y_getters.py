class Circle:
    def __init__(self, radius):
        self._radius = radius

    # Getter
    @property
    def radius(self):
        return self._radius

    # Setter
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # Deleter
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius

my_circle = Circle(33)
print("Initial radius:", my_circle.radius)  # 33

# Delete the radius
# This calls the deleter
del my_circle.radius # Deleting radius...
print("Radius deleted!") # Radius deleted!

# Try to access radius after deletion
try:
    print(my_circle.radius)
except AttributeError as e:
    print("Error:", e) # Error: 'Circle' object has no attribute '_radius'