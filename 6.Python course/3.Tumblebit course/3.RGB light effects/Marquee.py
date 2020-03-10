from microbit import *
import neopixel
import microbit
Red = (255, 0, 0)
Orange = (255, 165, 0)
Yellow = (255, 255, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Violet = (148, 0, 211)
White = (255, 255, 255)
color_lib = {
        'Red': Red, 'Orange': Orange, 'Yellow': Yellow, 'Green': Green,
        'Blue': Blue, 'Violet': Violet, 'White': White
            }
# Function is used to set a single RGB light to a certain color,
# parameter num: set the actual position of the light (0-3)
# Parameter color: Set the color of the light.
# The color tuples in the color_lib dictionary are also defined.
def RGBLight_show(num, color):
    global np
    np[num] = color_lib[color]

np = neopixel.NeoPixel(pin12, 4)
display.show(Image.HEART)
while True:
    np.clear()
    RGBLight_show(0, 'Violet')
    RGBLight_show(1, 'Red')
    RGBLight_show(2, 'Green')
    RGBLight_show(3, 'Blue')
    np.show()
    microbit.sleep(100)
    np.clear()
    RGBLight_show(0, 'Blue')
    RGBLight_show(1, 'Violet')
    RGBLight_show(2, 'Red')
    RGBLight_show(3, 'Green')
    np.show()
    microbit.sleep(100)
    np.clear()
    RGBLight_show(0, 'Green')
    RGBLight_show(1, 'Blue')
    RGBLight_show(2, 'Violet')
    RGBLight_show(3, 'Red')
    np.show()
    microbit.sleep(100)
    np.clear()
    RGBLight_show(0, 'Red')
    RGBLight_show(1, 'Green')
    RGBLight_show(2, 'Blue')
    RGBLight_show(3, 'Violet')
    np.show()
    microbit.sleep(100)