from PIL import Image
import numpy as np
import sys


def get_mosaic_image(image, size=10, gradation=5):
    threshold = 255 // gradation
    width = len(image)
    height = len(image[0])
    x = 0
    while x < width:
        y = 0
        while y < height:
            sector = image[x: x + size, y: y + size]
            colors_sum_avg = np.sum(sector) / 3
            average_color = int(colors_sum_avg // (size * size))
            set_color(int(average_color // threshold) * threshold, image, size, x, y)
            y += size
        x += size
    return Image.fromarray(np.uint8(image))


def set_color(new_color, image, size, x, y):
    for sector_x in range(x, x + size):
        for sector_y in range(y, y + size):
            for c in range(3):
                image[sector_x][sector_y][c] = new_color


if __name__ == "__main__":
    source_name = sys.argv[1]
    output_name = sys.argv[2]

    source_img = Image.open(source_name)
    image_arr = np.array(source_img).astype(int)
    get_mosaic_image(image_arr, 1, 50).save(output_name)