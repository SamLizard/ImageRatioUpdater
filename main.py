import math
from PIL import Image
import os
from pathlib import Path

IMAGE_NAME = "6.m.a.DALL·E 2022-09-13 23.02.24 - fantaisy world, unreal engine 5, photo realism, octane render, megapixel"
IMAGE_EXTENSION = "." + "png"
FOLDER_PATH = "/Users/samuel/Documents/AI photo generation/Wallpaper/Dalle2/Outpainting/"


def main():
    output_image = resize_one_image()
    # show_output_images(output_image)

    # output_images = resize_folder_images("Standard ratio images")
    # show_output_images(*output_images)


def resize_folder_images(new_saving_folder_name=""):
    global IMAGE_NAME
    output_images = []
    new_folder_path = f"{FOLDER_PATH}{new_saving_folder_name}"

    if new_folder_path != "":
        os.mkdir(new_folder_path)

    for file in os.listdir(FOLDER_PATH):
        IMAGE_NAME = os.fsdecode(file).split(IMAGE_EXTENSION)[0]
        if IMAGE_NAME != ".DS_Store" and IMAGE_NAME != new_saving_folder_name:
            output_images.append(resize_one_image(f"{FOLDER_PATH}{new_saving_folder_name}"))

    return output_images


def resize_one_image(saving_path=str(Path.home() / "Downloads")):
    resizing_ratio, image = find_ratio()
    output_image = resize_image(resizing_ratio, image)
    output_image.save(f"{saving_path}/{IMAGE_NAME}{IMAGE_EXTENSION}")
    print(f"Image {IMAGE_NAME}{IMAGE_EXTENSION} has been saved in folder {saving_path}")
    return output_image


def find_ratio():
    path = r'' + f"{FOLDER_PATH}{IMAGE_NAME}{IMAGE_EXTENSION}"
    image = Image.open(path)
    width, height = image.size
    ratios = [(4, 5), (1, 1), (5, 4), (4, 3), (7, 5), (3, 2), (5, 3), (16, 9), (1.9, 1), (1.91, 1), (1000, 0.00001)]
    index = 0

    while width/height > ratios[index][0]/ratios[index][1] and index <= len(ratios):
        index += 1

    print(f"Needed ratio is: {ratios[index][0]}:{ratios[index][1]}")
    return (math.ceil(height * ratios[index][0] / ratios[index][1]), height), image


def resize_image(resizing_ratio: tuple[int, int], image):
    result = Image.new(image.mode, (resizing_ratio[0], resizing_ratio[1]), (0, 0, 0, 0))
    result.paste(image, (math.ceil(abs(image.size[0]-resizing_ratio[0])/2), math.ceil(abs(image.size[1]-resizing_ratio[1])/2)))
    return result


def show_output_images(*output_images):
    for output_image in output_images:
        output_image.show()


if __name__ == '__main__':
    main()
