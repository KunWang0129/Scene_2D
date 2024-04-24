class Shape:
    def __init__(self, color='black', rotation=0):
        self.position = (0,0)
        self.color = color
        self.rotation = rotation  # Rotation in degrees

    def place_shape_global(self, position):
        self.position = position

    def place_shape_local(self, reference_shape, position):
        ref_x, ref_y = reference_shape.position
        offset = 0
        if position == 'left':
            new_x = ref_x - offset - self.dimension
            new_y = ref_y
        elif position == 'right':
            new_x = ref_x + reference_shape.dimension + offset
            new_y = ref_y
        elif position == 'above':
            new_y = ref_y - offset - self.dimension
            new_x = ref_x
        elif position == 'below':
            new_y = ref_y + reference_shape.dimension + offset
            new_x = ref_x
        self.place_shape_global((new_x, new_y))

class Circle(Shape):
    def __init__(self, radius, color='black', rotation=0):
        super().__init__( color, rotation)
        self.radius = radius
        self.dimension = radius * 2

class Rectangle(Shape):
    def __init__(self, width, height, color='black', rotation=0):
        super().__init__( color, rotation)
        self.width = width
        self.height = height
        self.dimension = max(width, height)

class Triangle(Shape):
    def __init__(self, size, color='black', rotation=0):
        super().__init__( color, rotation)
        self.size = size
        self.dimension = size
