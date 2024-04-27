class Shape:
    def __init__(self, color="black", rotation=0):
        self.position = (0, 0)
        self.color = color
        self.rotation = rotation  # Rotation in degrees

    def place_shape_global(self, position):
        """
        This method places the shape at a global position specified by the 'position' parameter.

        Parameters:
        position (tuple): A tuple containing the x and y coordinates where the shape will be placed.

        Returns:
        None
        """
        self.position = position
        return None

    def place_shape_local(self, reference_shape, position):
        ref_x, ref_y = reference_shape.position
        offset = (self.dimension + reference_shape.dimension) // 2
        if position == "left":
            new_x = ref_x - offset
            new_y = ref_y
        elif position == "right":
            new_x = ref_x + offset
            new_y = ref_y
        elif position == "above":
            new_y = ref_y - offset
            new_x = ref_x
        elif position == "below":
            new_y = ref_y + offset
            new_x = ref_x
        self.place_shape_global((new_x, new_y))


class Circle(Shape):
    def __init__(self, radius, color="black", rotation=0):
        """
        This is a constructor for the Circle class which inherits from the Shape class.

        Parameters:
        radius (float): The radius of the circle.
        color (str, optional): The color of the circle. Defaults to 'black'.
        rotation (int, optional): The rotation of the circle in degrees. Defaults to 0.
        """
        super().__init__(color, rotation)
        self.radius = radius
        self.dimension = radius * 2


class Rectangle(Shape):
    def __init__(self, width, height, color="black", rotation=0):
        """
        This is a constructor for the Rectangle class which inherits from the Shape class.

        Parameters:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        color (str, optional): The color of the rectangle. Defaults to 'black'.
        rotation (int, optional): The rotation of the rectangle in degrees. Defaults to 0.
        """
        super().__init__(color, rotation)
        self.width = width
        self.height = height
        self.dimension = max(width, height)


class Triangle(Shape):
    def __init__(self, size, color="black", rotation=0):
        """
        This is a constructor for the Triangle class which inherits from the Shape class.

        Parameters:
        size (float): The size of the triangle, which is used as the length of its sides.
        color (str, optional): The color of the triangle. Defaults to 'black'.
        rotation (int, optional): The rotation of the triangle in degrees. Defaults to 0.
        """
        super().__init__(color, rotation)
        self.size = size
        self.dimension = size
        # self.height = size * (3 ** 0.5) / 2
