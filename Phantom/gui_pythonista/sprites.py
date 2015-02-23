# -*- coding: utf-8 -*-

"""Load images into a scene-usable image."""

import scene
import os

folder = 'imgs'
format = 'Chess set images {} {}.jpg'

files = [os.path.join(folder, format.format(color, type))
         for type in ('pawn', 'rook', 'queen', 'king', 'bishop', 'knight')
         for color in ('black', 'white')]

img_names = {}
for file in files:
    name = os.path.split(file)[1]
    img = scene.load_image_file(file)
    img_names.update({name: img})

if __name__ == '__main__':
    for key in img_names:
        print key, img_names[key]

