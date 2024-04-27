from PIL import Image, ImageDraw
from utils.Shape import Circle, Rectangle, Triangle


class Scene:
    """
    This class represents a scene where shapes can be added, removed, and rendered into an image.

    Attributes:
    size (tuple): The size of the scene as a tuple of width and height.
    bg_color (str): The background color of the scene.
    shapes (list): A list of shapes added to the scene.
    """

    def __init__(self, size=(800, 600), bg_color="white"):
        """
        This is a constructor for the Scene class.

        Parameters:
        size (tuple, optional): The size of the scene as a tuple of width and height. Defaults to (800, 600).
        bg_color (str, optional): The background color of the scene. Defaults to 'white'.
        """
        self.size = size
        self.bg_color = bg_color
        self.shapes = []

    def add_shape(self, shape):
        """
        This method adds a shape to the scene.

        Parameters:
        shape (Shape): The shape to be added to the scene.

        Returns:
        None
        """
        self.shapes.append(shape)

    def remove_shape(self, shape):
        """
        This method removes a shape from the scene.

        Parameters:
        shape (Shape): The shape to be removed from the scene.

        Returns:
        None
        """
        self.shapes.remove(shape)

    def create_background(self):
        """
        This method creates a new image with the size and background color of the scene.

        Returns:
        Image: A new image with the size and background color of the scene.
        """
        return Image.new("RGB", self.size, self.bg_color)

    def render(self, filename="scene.png"):
        """
        This method renders the scene into an image file.

        Parameters:
        filename (str, optional): The name of the image file. Defaults to 'scene.png'.

        Returns:
        None
        """
        image = self.create_background()
        draw = ImageDraw.Draw(image)

        for shape in self.shapes:
            if isinstance(shape, Circle):
                self.draw_circle(draw, shape)
            elif isinstance(shape, Rectangle):
                self.draw_rectangle(draw, shape)
            elif isinstance(shape, Triangle):
                self.draw_triangle(draw, shape)

        image.save(filename)

    def draw_circle(self, draw, circle):
        """
        This method draws a circle on the scene.

        Parameters:
        draw (ImageDraw.Draw): The drawing context.
        circle (Circle): The circle to be drawn.

        Returns:
        None
        """
        left_up = (
            circle.position[0] - circle.radius,
            circle.position[1] - circle.radius,
        )
        right_down = (
            circle.position[0] + circle.radius,
            circle.position[1] + circle.radius,
        )
        draw.ellipse([left_up, right_down], outline=circle.color, fill=circle.color)

    def draw_rectangle(self, draw, rectangle):
        """
        This method draws a rectangle on the scene.

        Parameters:
        draw (ImageDraw.Draw): The drawing context.
        rectangle (Rectangle): The rectangle to be drawn.

        Returns:
        None
        """
        cx, cy = rectangle.position
        width, height = rectangle.width, rectangle.height
        # Calculate half of the width and height
        half_width, half_height = width / 2, height / 2

        # Calculate the coordinates of the rectangle (non-rotated) from the center
        coords = [
            cx - half_width,
            cy - half_height,  # Top-left
            cx + half_width,
            cy - half_height,  # Top-right
            cx + half_width,
            cy + half_height,  # Bottom-right
            cx - half_width,
            cy + half_height,  # Bottom-left
        ]

        if rectangle.rotation != 0:
            # If rotation is applied, calculate the new coordinates
            coords = self.rotate_coords(coords, rectangle.rotation, (cx, cy))

        draw.polygon(coords, outline=rectangle.color, fill=rectangle.color)

    def draw_triangle(self, draw, triangle):
        cx, cy = triangle.position
        size = triangle.size

        # Assuming an equilateral triangle, calculate the initial coordinates
        height = size * (3**0.5) / 2  # Height of equilateral triangle
        coords = [
            (cx, cy - 2 / 3 * height),  # Top vertex
            (cx - size / 2, cy + 1 / 3 * height),  # Bottom left vertex
            (cx + size / 2, cy + 1 / 3 * height),  # Bottom right vertex
        ]

        if triangle.rotation != 0:
            # Convert list of tuples to a flat list for rotation
            flat_coords = [coord for point in coords for coord in point]
            # If rotation is applied, calculate the new coordinates
            flat_coords = self.rotate_coords(flat_coords, triangle.rotation, (cx, cy))
            # Convert flat list back to list of tuples
            coords = [
                (flat_coords[i], flat_coords[i + 1])
                for i in range(0, len(flat_coords), 2)
            ]

        # Draw the triangle using the polygon method with three points
        draw.polygon(coords, outline=triangle.color, fill=triangle.color)

    def rotate_coords(self, coords, angle, center):
        """
        This method rotates a set of coordinates around a center point.

        Parameters:
        cx (float): The x-coordinate of the center point.
        cy (float): The y-coordinate of the center point.
        coords (list): A list of tuples representing the coordinates to be rotated.
        angle (float): The angle of rotation in degrees.

        Returns:
        list: A list of tuples representing the rotated coordinates.
        """
        from math import radians, sin, cos

        angle = radians(
            -angle
        )  # Convert angle from degrees to radians, negate for clockwise rotation
        cx, cy = center
        new_coords = []

        # Assuming coords is a flat list [x0, y0, x1, y1, ..., xn, yn]
        for i in range(0, len(coords), 2):
            x, y = coords[i], coords[i + 1]
            # Translate point to origin
            temp_x, temp_y = x - cx, y - cy
            # Rotate point
            rotated_x = temp_x * cos(angle) - temp_y * sin(angle)
            rotated_y = temp_x * sin(angle) + temp_y * cos(angle)
            # Translate point back
            new_x, new_y = rotated_x + cx, rotated_y + cy
            new_coords.extend([new_x, new_y])

        return new_coords
