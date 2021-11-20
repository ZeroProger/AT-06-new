import os.path

from PIL import Image
import numpy as np
import sys


def get_mosaic_image(image, size=10, gradation=5):
    threshold = 255 // gradation
    height = len(image)
    width = len(image[0])
    x = 0
    while x < height:
        y = 0
        while y < width:
            sector = image[x: x + size, y: y + size]
            colors_sum_avg = np.sum(sector) / 3
            average_color = int(colors_sum_avg // (size * size))
            set_color(int(average_color // threshold) * threshold, image, size, x, y)
            y += size
        x += size
    print('Ширина изображения: ', width)
    print('Высота изображения: ', height)
    print('Тип изображения:', output_name.split('.')[1])
    print('Размер элемента мозаики: ', size)
    print('Кол-во градаций серого: ', gradation)
    return Image.fromarray(np.uint8(image))


def set_color(new_color, image, size, x, y):
    for sector_x in range(x, x + size):
        for sector_y in range(y, y + size):
            for c in range(3):
                image[sector_x][sector_y][c] = new_color


if __name__ == "__main__":
    source_name = input("Введите имя файла входного изображения: ")
    output_name = input("Введите имя выходного файла: ")

    source_img = Image.open(source_name)
    image_arr = np.array(source_img).astype(int)
    get_mosaic_image(image_arr, 5, 50).save(output_name)
    if os.path.exists(output_name):
        print('Изображение изменено')
