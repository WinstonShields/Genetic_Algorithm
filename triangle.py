import random


class Triangle:
    # Initialize constructor for triangle.
    def __init__(self):
        self._a = []
        self._b = []
        self._c = []
        self._color = []

    # Getter for point A.
    @property
    def a(self):
        return self._a

    # Setter for point A.
    @a.setter
    def a(self, value):
        self._a = value

    # Getter for point A.
    @property
    def b(self):
        return self._b

    # Setter for point A.
    @b.setter
    def b(self, value):
        self._b = value

    # Getter for point A.
    @property
    def c(self):
        return self._c

    # Setter for point A.
    @c.setter
    def c(self, value):
        self._c = value

    # Getter for the triangle color.
    @property
    def color(self):
        return self._color

    # Setter for the triangle color.
    @color.setter
    def color(self, value):
        self._color = value

    def forms_triangle(self, ax, ay, bx, by, cx, cy):
        # Verify if the coordinates form a triangle. Not all x
        # coordinates can be the same, and not all y coordinates
        # can be the same, or a straight line would be formed.
        if (ax != bx and ax != cx and bx != cx and
                ay != by and ay != cy and by != cy):
            return True

    def create_triangle(self, ax, ay, bx, by, cx, cy, red, green, blue):
        if self.forms_triangle(ax, ay, bx, by, cx, cy):
            # If the coordinates successfully form a triangle, set up the triangle.

            # Give the triangle the coordinates that were randomly generated.
            self.a = [ax, ay]
            self.b = [bx, by]
            self.c = [cx, cy]

            # Set the RGB values to the triangle color.
            self.color = [red, green, blue]

            return True
        else:
            # If no triangle is formed, return none.
            return False

    def __str__(self):
        return f"A: {self.a}, B: {self.b}, C: {self.c}, RGB: {self.color}"
