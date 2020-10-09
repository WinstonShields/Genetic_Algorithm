import math
import os
from PIL import Image, ImageDraw


def fitness(target_img, generated_img):
    # Initialize total color difference variable.
    total_color_diff = 0

    for pixel_x in range(target_img.size[0]):
        for pixel_y in range(target_img.size[1]):
            # Set the target images RGB values.
            target_r, target_g, target_b = target_img.getpixel(
                (pixel_x, pixel_y))

            # Set the generated images RGB values.
            gen_r, gen_g, gen_b = generated_img.getpixel(
                (pixel_x, pixel_y))

            # Get the difference of the generated pixel's RGB compared
            # to the target image's pixel RGB.
            diff_r = abs(gen_r - target_r)
            diff_g = abs(gen_g - target_g)
            diff_b = abs(gen_b - target_b)

            # Get the color difference between the target image's pixel and
            # the generated images pixel.
            # Color Difference = √((|R2 - R1|)^2 + (|G2 - G1|)^2 + (|B1 - B2|)^2)
            color_diff = math.sqrt((diff_r**2) + (diff_g**2) + (diff_b**2))

            # Add color difference to total color difference.
            total_color_diff += color_diff

    # Return the total color difference.
    return total_color_diff


def selection(target_img, i, image_data_list):
    # Initialize a dictionary of color differences.
    color_diff_dict = {}

    for image in os.listdir("generated_images"):
        # Get the total color difference of each pixel from the target
        # image and each generated image.
        total_color_diff = fitness(target_img.convert("RGB"),
                                   Image.open("generated_images/" + image).convert("RGB"))

        # Add the image to the dictionary of color differences with the key value being
        # the the image generated, and the value being the color difference total.
        color_diff_dict[image] = total_color_diff

    # Sort the dictionary by color difference and convert it into a list.
    sorted_color_diff = sorted(color_diff_dict.items(), key=lambda x: x[1])

    # Set the two parents for reproduction as the two images with the lowest total
    # color differences. The parent value will be the numeric ID in front of the
    # file extension.
    parent_1 = int(sorted_color_diff[0][0].split('.')[0])
    parent_2 = int(sorted_color_diff[1][0].split('.')[0])

    # Return the two parents for reproduction.
    return [parent_1, parent_2]
