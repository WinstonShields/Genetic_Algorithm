from triangle import Triangle
from PIL import Image, ImageDraw


class Individual:
    def __init_(self):
        self._id = 0
        self._triangles = []
        self._fitness = 0
        self._image = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def triangles(self):
        return self._triangles

    @triangles.setter
    def triangles(self, value):
        self._triangles = value

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, value):
        self._fitness = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    def create_image(self, img_width, img_height):
       # Create image object with the same dimensions as the original
        # image.
        img = Image.new('RGB', (img_width, img_height))

        background_draw = ImageDraw.Draw(img)

        background_draw.polygon(
            [(0, 0), (0, img_height), (img_width, img_height), (img_width, 0)], (255, 255, 255, 255))

        # Create draw object with alpha channel (so that image can be translucent).
        draw = ImageDraw.Draw(img, 'RGBA')

        for triangle in self.triangles:
            # Draw each triangle in the list of genes.
            draw.polygon([(triangle.a[0], triangle.a[1]), (triangle.b[0], triangle.b[1]),
                          (triangle.c[0], triangle.c[1])],
                         (triangle.color[0], triangle.color[1], triangle.color[2], 100))

        # Set image drawn to the individual.
        self.image = img
