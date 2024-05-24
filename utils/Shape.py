class Shape:
    def __init__(self, color="black"):
        self.position = (0, 0)
        self.color = color

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

    def place_shape_local(self, reference_shape, position, offset=(0, 0)):
        """
        Place the shape adjacent to a reference shape.

        Parameters:
        reference_shape : Shape
            The shape to use as the reference for positioning.
        position : str
            The desired position adjacent to the reference shape. Can only be one of: "left", "right", "above", "below", "center".
        offset : tuple of int, optional
            A tuple (x_offset, y_offset) that specifies additional offset to apply to the final position.
            A positive x value moves the shape to the right, a negative x value moves the shape to the left.
            A positive y value moves the shape down, a negative y value moves the shape up.

        Returns:
        None
        """

        ref_x, ref_y = reference_shape.position
        initial_offset = self.dimension[1]

        self_dim = self.dimension
        ref_dim = reference_shape.dimension
        if self.__class__.__name__ == "Triangle":
            if position == "above":
                self_dim = (self_dim[0], self_dim[1]/(3**0.5))
            elif position == "below":
                self_dim = (self_dim[0], 2*self_dim[1]/(3**0.5))
        if reference_shape.__class__.__name__ == "Triangle":
            if position == "above":
                ref_dim = (ref_dim[0], 2*ref_dim[1]/(3**0.5))
            elif position == "below":
                ref_dim = (ref_dim[0], ref_dim[1]/(3**0.5))
        
        offset_x = (self_dim[0] + ref_dim[0]) // 2
        offset_y = (self_dim[1] + ref_dim[1]) // 2


        # ref_x, ref_y = reference_shape.position
        # initial_offset = self.dimension[1]
        # # TODO: replace with simpler code
        # if self.__class__.__name__ == "Triangle":
        #     print(f"Initial offset = {initial_offset}")
        #     is_above = -1 if position == "above" else 1
        #     if position == "above":
        #         triangle_offset = (initial_offset * 3 ** 0.5) / 3
        #     else:
        #         triangle_offset = (initial_offset * 3 ** 0.5) / 2
        #     diff = initial_offset - triangle_offset
        #     initial_offset += diff * is_above
        #     print(f"final offset = {initial_offset}")
        # if reference_shape.__class__.__name__ == "Triangle":
        #     ref_y = 0.5 * (ref_y * 3 ** 0.5)

        # offset_x = (self.dimension[0] + reference_shape.dimension[0]) // 2
        # offset_y = (initial_offset + reference_shape.dimension[1]) // 2

        if position == "left":
            new_x = ref_x - offset_x
            new_y = ref_y
        elif position == "right":
            new_x = ref_x + offset_x
            new_y = ref_y
        elif position == "above":
            new_y = ref_y - offset_y
            new_x = ref_x
        elif position == "below":
            new_y = ref_y + offset_y
            new_x = ref_x
        elif position== "center":
            new_x=ref_x
            new_y=ref_y
        else:
            print("Invalid Position!")
            print(position)
            
        new_x += offset[0]
        new_y += offset[1]

        self.place_shape_global((new_x, new_y))


class Circle(Shape):
    def __init__(self, radius, color="black"):
        """
        This is a constructor for the Circle class which inherits from the Shape class.

        Parameters:
        radius (float): The radius of the circle.
        color (str, optional): The color of the circle. Defaults to 'black'.
        """
        super().__init__(color)
        self.radius = radius
        self.dimension = (radius * 2, radius * 2)


class Rectangle(Shape):
    def __init__(self, width, height, color="black"):
        """
        This is a constructor for the Rectangle class which inherits from the Shape class.

        Parameters:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        color (str, optional): The color of the rectangle. Defaults to 'black'.
        """
        super().__init__(color)
        self.width = width
        self.height = height
        self.dimension = (width, height)


class Triangle(Shape):
    def __init__(self, size, color="black"):
        """
        This is a constructor for the Triangle class which inherits from the Shape class.

        Parameters:
        size (float): The size of the triangle, which is used as the length of its sides.
        color (str, optional): The color of the triangle. Defaults to 'black'.
        """
        super().__init__(color)
        self.size = size
        self.dimension = (size, size)
