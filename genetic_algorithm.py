from triangle import Triangle
from individual import Individual
import random
import math
import operator
from PIL import Image
import copy


def initial_population(img_width, img_height, initial_pop_size, num_of_triangles):
    # Initialize list of individuals.
    individuals = []

    for i in range(initial_pop_size):
        # Initialize list of triangles
        triangles = []

        for j in range(num_of_triangles):
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

            triangle_created = False

            if triangle.create_triangle(ax, ay, bx, by, cx, cy, red, green, blue):
                # If triangle is successfully created, append it to a list of triangles.
                triangles.append(triangle)
                triangle_created = True

            else:
                while not triangle_created:
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

                    if triangle.create_triangle(ax, ay, bx, by, cx, cy, red, green, blue):
                        # If triangle is successfully created, append it to a list of triangles.
                        triangles.append(triangle)
                        triangle_created = True

        # Create a new individual.
        individual = Individual()
        individual.id = len(individuals)

        # Set the list of triangles into the individual.
        individual.triangles = triangles

        # Create an image for the triangle.
        individual.create_image(img_width, img_height)

        # Append the individual to the list of individuals.
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
        individual.fitness = fitness(target_img.convert(
            "RGB"), individual.image.convert("RGB"))

    # Sort the list of individuals from lowest fitness score to highest.
    individuals = sorted(
        individuals, key=operator.attrgetter('fitness'), reverse=False)

    # Set the parents for reproduction to the first two individuals in the
    # sorted individual list, because they are the individuals with the
    # lowest total color difference (best fitness value).
    parent_1 = individuals[0]
    parent_2 = individuals[1]

    return [parent_1, parent_2]


def reproduction(parent_1, parent_2, population_size, num_of_triangles, id, crossover_rate, mutation_rate, mutation_amount, img_width, img_height):
    # Initialize a list of children.
    children = []

    # Get the number of crossovers based on the crossover rate.
    crossovers = int(population_size * crossover_rate)

    # Make a set of randomized children that will result from crossovers, with the
    # size being based off of the crossover rate.

    crossover_set = set(random.sample(range(0, population_size), crossovers))

    # Get the number of mutations based on the mutation rate.
    mutations = int(population_size * mutation_rate)

    # Make a set of randomized children that will mutate, with the
    # size being based off of the crossover rate.
    print(mutations)
    mutation_set = set(random.sample(range(0, population_size), mutations))

    for i in range(population_size):
        # Initialize a child individual.
        child = Individual()
        child.id = id
        child.triangles = []

        parent_1_triangles = []
        parent_2_triangles = []

        if crossovers == 0 or i not in crossover_set:
            # If there are no crossovers, or this child is not in the crossover list,
            # just use one parent.
            parent_1_triangles = copy.deepcopy(parent_1.triangles)

        if crossovers != 0 and i in crossover_set:
            # If there are crossovers, get a random number of triangles to select from each parent.
            select_size = random.randint(1, num_of_triangles - 1)

            parent_1_triangles = random.sample(parent_1.triangles, select_size)

            parent_2_triangles = random.sample(
                parent_2.triangles, num_of_triangles - select_size)

        # Append the selected triangles from parent 1 into the child.
        for triangle in parent_1_triangles:
            child.triangles.append(triangle)

        if parent_2_triangles:
            # If the list of parent 2 triangles is not empty, append the triangles
            # into the child.
            for triangle in parent_2_triangles:
                child.triangles.append(triangle)

        if mutations != 0 and i in mutation_set:
            # If there are mutations, mutate the child.
            child = mutation(child, mutation_amount, img_width, img_height)

        child.create_image(img_width, img_height)

        # Append the child to the list of children.
        children.append(child)

        id += 1

    return children


def mutation(individual, mutation_amount, img_width, img_height):
    # Mutate the specified amount of times.
    for x in range(int(len(individual.triangles)*mutation_amount)):
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

        # Mutate the individual.
        if triangle.create_triangle(ax, ay, bx, by, cx, cy, red, green, blue):
            individual.triangles[random.randint(
                0, len(individual.triangles) - 1)] = triangle

    return individual
