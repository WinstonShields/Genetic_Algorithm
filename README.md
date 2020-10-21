# Genetic_Algorithm
This program uses a genetic algorithm to replicate a target image with triangles. 
The genetic operations include a fitness function, crossover, asexual reproduction,
and mutations.
The idea was inspired by the following blog:

<a href=https://rogerjohansson.blog/2008/12/07/genetic-programming-evolution-of-mona-lisa/> 
Genetic Programming: Evolution of Mona Lisa </a>

## Dependencies
Python 3

If you do not have the pip installer, you will need to install it.
Type this command in the terminal:
```bash
python get-pip.py
```
In your terminal, use the package manager pip install Pillow.
```bash
pip install Pillow
```

## Usage
Run the program by typing in the terminal in the following format:
```bash
# "population size" and "num of triangles" should be an integer. "crossover rate", "mutation rate", and
# "mutation amount" must be decimals between 0 and 1.
py main.py [target image] [population size] [num of triangles] [crossover rate] [mutation rate] [mutation amount]

# For example, type this to replicate an image by the name "mona_lisa.jpg" with a population size of 20,
# 100 triangles, a crossover rate of 0.1, mutation rate of 0.7, and a mutation amount of 0.1.
py main.py mona_lisa.jpg 20 100 0.1 0.7 0.1
```
## Parameters
* Target Image: The image that will be replicated.
* Population Size: Number of individuals in a generation.
* Number of Triangles: The number of triangles present in an individual/image.
* Crossover Rate: Percentage of individuals that reproduce sexually or asexually (The closer to 1, the more reproduced sexually).
* Mutation Rate: Percentage of how many individuals get mutated.
* Mutation Amount: Percentage of how many triangles in an individual get

## Results
The replicated images will be saved in the newly created "generated_images" directory. It will save an image in every 20
iterations.
