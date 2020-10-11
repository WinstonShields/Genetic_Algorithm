from triangle import Triangle
import genetic_algorithm
from PIL import Image, ImageDraw
import random
import turtle
import sys
import os


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


def initial_population(img_width, img_height):
    # Initialize a list of lists that contain the triangles inside an image.
    image_data_list = []

    for x in range(10):
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

            # Randomly generate RGB values.
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)

            # Create a triangle.
            triangle = Triangle.create_triangle(
                Triangle, ax, ay, bx, by, cx, cy, red, green, blue)

            if triangle is not None:
                # If a triangle was created, append it to the list of triangles.
                triangles.append(triangle)

                # Increment the counter.
                i = i + 1

        # Call the create image function.
        create_image(triangles, img_width, img_height, x)

        # Append the list of triangles to the list of image data.
        image_data_list.append(triangles)

    # Return the list of images generated and the most recent image index.
    return [image_data_list, x]


def get_image(img_name):
    return Image.open(img_name)


if __name__ == "__main__":
    # Get the target image by command line argument.
    target_img = get_image(sys.argv[1])

    width, height = target_img.size

    if not os.path.exists("generated_images"):
        os.makedirs("generated_images")

    # Call the initial population function and set the image data list and the most
    # recent image index.
    image_data_list, i = initial_population(width, height)

    while True:

        # Call the selection function and retrieve the two parent ID's for reproduction.
        parent_1, parent_2 = genetic_algorithm.selection(
            target_img, i, image_data_list)

        # Retrieve an offspring reproduced by the crossover of parent 1 and parent 2.
        offspring = genetic_algorithm.crossover(parent_1, parent_2)

        # Mutate the offspring of the parents.
        mutated_offspring = genetic_algorithm.mutation(offspring, width, height)

        image_data_list.append(mutated_offspring)

        new_image = []

        for triangle in parent_1:
            new_image.append(triangle)

        for triangle in parent_2:
            new_image.append(triangle)

        for triangle in mutated_offspring:
            new_image.append(triangle)

        create_image(new_image, width, height, i)

        i = i + 1

