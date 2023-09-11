from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from PIL import Image

"""
This class generates a 2D array (map) from an image file. 

1-Convert image to grayscale.
2-Get width, height.
3-Load pixel data.
4-Check each pixel value against threshold.
5-Set corresponding array value to 0 or 1.
6-Return the completed 2D array.
"""

class image_to_array:

    def generateMap(self , filename):
        with Image.open(filename).convert('L') as img:
            width, height = img.size
            pixels = img.load()
            array = [[1 if pixels[x, y] < 128 else 0 for x in range(width)] for y in range(height)]
        return array