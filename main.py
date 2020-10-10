from triangle import Triangle
import genetic_algorithm
from PIL import Image, ImageDraw
import random
import turtle
import sys
import os


def forms_triangle(ax, ay, bx, by, cx, cy):
    # Verify if the coordinates form a triangle. Not all x
    # coordinates can be the same, and not all y coordinates
    # can be the same, or a straight line would be formed.
    if (ax != bx and ax != cx and bx != cx and
            ay != by and ay != cy and by != cy):
        return True


def create_image(triangles, img_width, img_height, num):
    # Create image object with the same dimensions as the original
    # image.
    img = Image.new('RGB', (img_width, img_height))

    # Create draw object with alpha channel (so that image can be translucent).
    draw = ImageDraw.Draw(img, 'RGBA')

    for triangle in triangles:
        # Draw each triangle in the list of triangles.
        draw.polygon([(triangle.a[0], triangle.a[1]), (triangle.b[0], triangle.b[1]),
                      (triangle.c[0], triangle.c[1])],
                     (triangle.color[0], triangle.color[1], triangle.color[2], 100))

    # Save the drawings to an image.
    img.save(f"generated_images/{num}.jpg", 'JPEG')


def initial_population(img_width, img_height, n):
    # Initialize a list of lists that contain the triangles inside an image.
    image_data_list = []

    for x in range(n):
        # Initialize a list of triangles.
        triangles = []

        # Initialize a counter.
        i = 0

        while True:
            if i == 10:
                # Stop creating triangles if counter is equal to 100.
                break

            # Randomly select a coordinate for each point: A, B, and C
            ax = random.randint(0, img_width)
            ay = random.randint(0, img_height)
            bx = random.randint(0, img_width)
            by = random.randint(0, img_height)
            cx = random.randint(0, img_width)
            cy = random.randint(0, img_height)

            if forms_triangle(ax, ay, bx, by, cx, cy):
                # If the coordinates successfully form a triangle, create a
                # new instance of a triangle.
                triangle = Triangle()

                # Give the triangle the coordinates that were randomly generated.
                triangle.a = [ax, ay]
                triangle.b = [bx, by]
                triangle.c = [cx, cy]

                # Randomly generate RGB values.
                red = random.randint(0, 255)
                blue = random.randint(0, 255)
                green = random.randint(0, 255)

                # Set the RGB values to the triangle color.
                triangle.color = [red, blue, green]

                # Append the triangle to the list of triangles.
                triangles.append(triangle)

                # Increment the counter.
                i += 1

        # Call the create image function.
        create_image(triangles, img_width, img_height, x)

        # Append the list of triangles to the list of image data.
        image_data_list.append(triangles)

    # Return the list of images generated and the most recent image index.
    return [image_data_list, i]


def main(img_name, n_population):
    return [Image.open(img_name), int(n_population)]


if __name__ == "__main__":
    # Get the target image by command line argument.
    target_img, n_population = main(sys.argv[1], sys.argv[2])

    width, height = target_img.size

    if not os.path.exists("generated_images"):
        os.makedirs("generated_images")

    # Call the initial population function and set the image data list and the most
    # recent image index.
    image_data_list, i = initial_population(width, height, n_population)

    # Call the selection function and retrieve the two parent ID's for reproduction.
    parent_1, parent_2 = genetic_algorithm.selection(
        target_img, i, image_data_list)

    genetic_algorithm.crossover(parent_1, parent_2)
