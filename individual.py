from triangle import Triangle
from PIL import Image, ImageDraw

# The individual is the object form of the image that is generated.


class Individual:

    def __init__(self):
        self._name = ''
        self._genes = []
        self._fitness = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def genes(self):
        return self._genes

    @genes.setter
    def genes(self, value):
        self._genes = value

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, value):
        self._fitness = value

    def create_image(self, img_width, img_height):
        # Create image object with the same dimensions as the original
        # image.
        img = Image.new('RGB', (img_width, img_height))

        # Create draw object with alpha channel (so that image can be translucent).
        draw = ImageDraw.Draw(img, 'RGBA')

        for triangle in self.genes:
            # Draw each triangle in the list of genes.
            draw.polygon([(triangle.a[0], triangle.a[1]), (triangle.b[0], triangle.b[1]),
                          (triangle.c[0], triangle.c[1])],
                         (triangle.color[0], triangle.color[1], triangle.color[2], 100))

        # Save the drawings to an image.
        img.save(f"generated_images/{self.name}", 'JPEG')

