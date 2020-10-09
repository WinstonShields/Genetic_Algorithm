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

    def __str__(self):
        return f"A: {self.a}, B: {self.b}, C: {self.c}, RGB: {self.color}"
