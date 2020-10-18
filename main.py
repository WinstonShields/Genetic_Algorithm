from triangle import Triangle
import genetic_algorithm
from PIL import Image
import sys
import os
import gc


def command_line_arg(target_img, population_size, num_of_triangles, crossover_rate, mutation_rate):
    if float(crossover_rate) > 1.0 or float(crossover_rate) < 0.0:
        print("Crossover rate must be between 0.0 and 1.0")
        exit(1)
    if float(mutation_rate) > 1.0 or float(crossover_rate) < 0.0:
        print("Mutation rate must be between 0.0 and 1.0")
        exit(1)

    return [Image.open(target_img), population_size, num_of_triangles, crossover_rate, mutation_rate]


if __name__ == "__main__":
    # Retrieve the target image, initial population size, and
    # number of triangles for each individual.
    target_img, population_size, num_of_triangles, crossover_rate, mutation_rate = command_line_arg(
        sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]))

    img_width, img_height = target_img.size

    if not os.path.exists("generated_images"):
        os.makedirs("generated_images")

    # Get the initial population of individuals.
    individuals = genetic_algorithm.initial_population(
        img_width, img_height, population_size, num_of_triangles)

    # Initialize a variable for the next individual ID.
    next_id = len(individuals) + 1

    # Get the parents selected for reproduction.
    parent_1, parent_2 = genetic_algorithm.selection(target_img, individuals)

    parent_1.image.save(f"generated_images/{parent_1.id}.jpg", 'JPEG')
    parent_2.image.save(f"generated_images/{parent_2.id}.jpg", 'JPEG')

    # Delete the individuals from memory to speed up the program.
    del individuals
    gc.collect()

    while True:

        # Retrieve the children individuals using the reproduction funciton call.
        children = genetic_algorithm.reproduction(
            parent_1, parent_2, population_size, num_of_triangles, next_id, crossover_rate, mutation_rate, img_width, img_height)

        parent_1, parent_2 = genetic_algorithm.selection(target_img, children)

        print(parent_1.fitness, parent_2.fitness)

        # Save every 20 individuals as images.
        if next_id % 20 == 0:
            parent_1.image.save(f"generated_images/{parent_1.id}.jpg", 'JPEG')
            parent_2.image.save(f"generated_images/{parent_2.id}.jpg", 'JPEG')

        # Delete the children to 
        del children
        gc.collect()

        # Increment the ID.
        next_id += 1
