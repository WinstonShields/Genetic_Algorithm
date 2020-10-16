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
            ax = random.randint(0, img_width + 20)
            ay = random.randint(0, img_height + 20)
            bx = random.randint(0, img_width + 20)
            by = random.randint(0, img_height + 20)
            cx = random.randint(0, img_width + 20)
            cy = random.randint(0, img_height + 20)

            # Randomly generate RGB values.
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)

            # Create a triangle.
            triangle = Triangle()

            if triangle.create_triangle(ax, ay, bx, by, cx, cy, red, green, blue):
                # If triangle is successfully created, append it to a list of triangles.
                triangles.append(triangle)

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


def crossover(parent_1, parent_2, population_size, num_of_triangles, id, img_width, img_height):
    # Initialize a list of children.
    children = [] 

    for i in range(population_size):
        # Get a random number of triangles to select from each parent.
        select_size = random.randint(1, num_of_triangles - 1)
        parent_1_triangles = random.sample(parent_1.triangles, select_size)

        #print(num_of_triangles - select_size)

        parent_2_triangles = random.sample(
            parent_2.triangles, num_of_triangles - select_size)


        # Initialize a child individual.
        child = Individual()
        child.id = id

        child.triangles = []

        # Append the selected triangles from each parent into the child.
        for triangle in parent_1_triangles:
            child.triangles.append(triangle)

        for triangle in parent_2_triangles:
            child.triangles.append(triangle)


        child.create_image(img_width, img_height)

        # Append the child to the list of children.
        children.append(child)

        # Create a mutated version of the child.
        mutated_child = Individual()
        mutated_child = copy.deepcopy(child)
        id += 1
        mutated_child.id = id
        mutated_child = mutation(mutated_child, img_width, img_height)

        mutated_child.create_image(img_width, img_height)

        # Append the child to the list of children.
        children.append(mutated_child)

        id += 1

    return children


def mutation(individual, img_width, img_height):
    # Make the mutation amount of the individual only 10%.
    for x in range(random.randint(1, int(len(individual.triangles)*0.10))):
        ax = random.randint(0, img_width + 20)
        ay = random.randint(0, img_height + 20)
        bx = random.randint(0, img_width + 20)
        by = random.randint(0, img_height + 20)
        cx = random.randint(0, img_width + 20)
        cy = random.randint(0, img_height + 20)

        red = random.randint(0, 255)
        blue = random.randint(0, 255)
        green = random.randint(0, 255)

        triangle = Triangle()

        # Mutate the individual.
        if triangle.create_triangle(ax, ay, bx, by, cx, cy, red, green, blue):
            individual.triangles[random.randint(
                0, len(individual.triangles) - 1)] = triangle

    return individual
