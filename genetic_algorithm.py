from triangle import Triangle
from individual import Individual
from PIL import Image, ImageDraw
import random
import math
import operator


def initial_population(img_width, img_height, initial_pop_size, num_of_triangles):
    # Initialize a list of individuals.
    individuals = []

    for x in range(initial_pop_size):
        # Initialize a list of triangles.
        triangles = []

        for num in range(num_of_triangles):

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
            triangle = Triangle()

            if triangle.create_triangle(ax, ay, bx, by, cx, cy, red, green, blue):
                # If triangle is successfully created, append it to a list of triangles.
                triangles.append(triangle)

        # Produce an individual.
        individual = Individual()

        # Append the triangles in the list of individual genes.
        for triangle in triangles:
            individual.genes.append(triangle)

        # Set the name of the individual.
        individual.name = f"{x}.jpg"

        # Create an image based off of the individual.
        individual.create_image(img_width, img_height)

        # Append each indivdual to the list of individuals.
        individuals.append(individual)

    return individuals


def fitness(target_img, individual_img):
    # Initialize the total color difference.
    total_color_diff = 0

    for pixel_x in range(target_img.size[0]):
        for pixel_y in range(target_img.size[1]):
            # Set the target images RGB values.
            target_r, target_g, target_b = target_img.getpixel(
                (pixel_x, pixel_y))

            # Set the individual's RGB values.
            individual_r, individual_g, individual_b = individual_img.getpixel(
                (pixel_x, pixel_y))

            # Get the difference of the individual's pixel's RGB compared to
            # the target images pixel.
            diff_r = abs(individual_r - target_r)
            diff_g = abs(individual_g - target_g)
            diff_b = abs(individual_b - target_b)

            # Get the color difference between the target image's pixel and
            # the generated images pixel.
            # Color Difference = √((|R2 - R1|)^2 + (|G2 - G1|)^2 + (|B1 - B2|)^2)
            color_diff = math.sqrt((diff_r**2) + (diff_g**2) + (diff_b**2))

            # Add color difference to total color difference.
            total_color_diff += color_diff

    return total_color_diff


def selection(target_img, individuals):

    for individual in individuals:
        # Set the individual's fitness value by calling the fitness function.
        individual.fitness = fitness(target_img.convert("RGB"), Image.open(
            "generated_images/" + individual.name).convert("RGB"))

    # Sort the list of individuals from lowest fitness score to highest.
    individuals = sorted(
        individuals, key=operator.attrgetter('fitness'), reverse=False)

    # Set the parents for reproduction to the first two individuals in the 
    # sorted individual list, because they are the individuals with the
    # lowest total color difference (best fitness value).
    parent_1 = individuals[0]
    parent_2 = individuals[1]

    return [parent_1, parent_2]

def crossover(parent_1, parent_2):
    # Randomly select half of the elements from each parent.
    parent_1_genes = random.sample(parent_1.genes, int(len(parent_1.genes)/2))
    parent_2_genes = random.sample(parent_2.genes, int(len(parent_2.genes)/2))

    # Create an offspring that will inherit  half of parent 1's
    # elements and half of parent 2's elements.
    offspring = Individual()

    # Append the genes from each parent into the offspring.
    for triangle in parent_1_genes:
        offspring.genes.append(triangle)

    for triangle in parent_2_genes:
        offspring.genes.append(triangle)

    return offspring

def mutation(offspring, img_width, img_height):
    for x in range(random.randint(1, 3)):

        ax = random.randint(0, img_width)
        ay = random.randint(0, img_height)
        bx = random.randint(0, img_width)
        by = random.randint(0, img_height)
        cx = random.randint(0, img_width)
        cy = random.randint(0, img_height)

        red = random.randint(0, 255)
        blue = random.randint(0, 255)
        green = random.randint(0, 255)

        triangle = Triangle()

        # In a random range from 1 to 3, generate a new triangle
        # with random attributes.
        if triangle.create_triangle(ax, ay, bx, by, cx, cy, red, green, blue):
            offspring.genes[random.randint(0, len(offspring.genes) - 1)] = triangle

    return offspring





