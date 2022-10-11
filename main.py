import math

from PIL import Image
import os

IMAGE_NAME = "6.m.a.DALL·E 2022-09-13 23.02.24 - fantaisy world, unreal engine 5, photo realism, octane render, megapixel"
IMAGE_EXTENSION = ".png"
FOLDER_PATH = "/Users/samuel/Documents/AI photo generation/Wallpaper/Dalle2/Outpainting/"

# with Image.open(path) as img:
# img.load()
# img.show()

# if 1 > width/height > 0.8 ==> 1:1
# if width/height < 0.8 ==> 4:5
# if width/height > 1 ==> 16:9


# indicator = width/height
# index_ratio = 1 if indicator <= 0.8 else 2 if indicator > 1 else 0


def main():
    # print(os.getcwd())
    # resizing_ratio, image = find_ratio()
    # output_image = resize_image(resizing_ratio, image)
    # print(os.listdir(FOLDER_PATH))
    output_images = resize_folder_images("Wallpaper_Croped_Photosop")
    # for output_image in output_images:
    #     output_image.show()


def resize_folder_images(new_saving_folder_name):
    global IMAGE_NAME
    output_images = []
    new_folder_path = f"{FOLDER_PATH}{new_saving_folder_name}"
    os.mkdir(new_folder_path)

    for file in os.listdir(FOLDER_PATH):
        IMAGE_NAME = os.fsdecode(file).split(".png")[0]
        if IMAGE_NAME != ".DS_Store" and IMAGE_NAME != new_saving_folder_name:
            resizing_ratio, image = find_ratio()
            output_images.append(resize_image(resizing_ratio, image))
            output_images[-1].save(f"{FOLDER_PATH}{new_saving_folder_name}/{IMAGE_NAME}{IMAGE_EXTENSION}")

    return output_images


def find_ratio():
    path = r'' + f"{FOLDER_PATH}{IMAGE_NAME}{IMAGE_EXTENSION}"
    image = Image.open(path)
    width, height = image.size
    ratios = [(4, 5), (1, 1), (5, 4), (4, 3), (7, 5), (3, 2), (5, 3), (16, 9), (1.9, 1), (1.91, 1), (1000, 0.00001)]
    index = 0

    while index < len(ratios):
        if width/height < ratios[index][0]/ratios[index][1]:
            break
        index += 1

    print(f"Needed ratio is: {ratios[index][0]}:{ratios[index][1]}")

    return (math.ceil(height * ratios[index][0] / ratios[index][1]), height), image


def resize_image(resizing_ratio: tuple[int, int], image):
    result = Image.new(image.mode, (resizing_ratio[0], resizing_ratio[1]), (0, 0, 0, 0))
    result.paste(image, (math.ceil(abs(image.size[0]-resizing_ratio[0])/2), math.ceil(abs(image.size[1]-resizing_ratio[1])/2)))  # (int(image.size[0]-resizing_ratio[0])/2, int(image.size[1]-resizing_ratio[1])/2))
    return result


if __name__ == '__main__':
    main()
