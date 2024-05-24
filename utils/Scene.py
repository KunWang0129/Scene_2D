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

    def render(self, filename="scene.png"):
        """
        This method renders the scene into an image file.

        Parameters:
        filename (str, optional): The name of the image file. Defaults to 'scene.png'.

        Returns:
        None
        """
        image = Image.new("RGB", self.size, self.bg_color)
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

        # Calculate the coordinates of the rectangle from the center
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

        # Draw the triangle using the polygon method with three points
        draw.polygon(coords, outline=triangle.color, fill=triangle.color)
