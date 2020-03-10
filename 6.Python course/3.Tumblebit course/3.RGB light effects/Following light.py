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

def RGBLight_show(num, color):
    global np
    np[num] = color_lib[color]

np = neopixel.NeoPixel(pin12, 4)
display.show(Image.HEART)
while True:
    np.clear()
    RGBLight_show(0, 'Violet')
    np.show()
    microbit.sleep(100)
    np.clear()
    RGBLight_show(1, 'Violet')
    np.show()
    microbit.sleep(100)
    np.clear()
    RGBLight_show(2, 'Violet')
    np.show()
    microbit.sleep(100)
    np.clear()
    RGBLight_show(3, 'Violet')
    np.show()
    microbit.sleep(100)