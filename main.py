from triangle import Triangle
import genetic_algorithm
from PIL import Image, ImageDraw
import random
import turtle
import sys
import os


def command_line_arg(img_name, initial_pop_size, num_of_triangles):
    return [Image.open(img_name), initial_pop_size, num_of_triangles]


if __name__ == "__main__":
    # Retrieve the target image, initial population size, and number
    # of triangles for each individual.
    target_img, initial_pop_size, num_of_triangles = command_line_arg(
        sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

    img_width, img_height = target_img.size

    if not os.path.exists("generated_images"):
        os.makedirs("generated_images")

    # Retrieve the individuals generated from the initial population 
    # function call.
    individuals = genetic_algorithm.initial_population(
        img_width, img_height, initial_pop_size, num_of_triangles)

    while True:

        parent_1, parent_2 = genetic_algorithm.selection(target_img, individuals)

        offspring = genetic_algorithm.crossover(parent_1, parent_2)

        mutated_offspring = genetic_algorithm.mutation(offspring, img_width, img_height)

        mutated_offspring.name = f"{len(individuals)}.jpg"

        individuals.append(mutated_offspring)

        mutated_offspring.create_image(img_width, img_height)
