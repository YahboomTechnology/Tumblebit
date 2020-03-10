from microbit import *
import microbit
import superbit

display.show(Image.HAPPY)

while True:
    superbit.motor_control_dual(superbit.M1, superbit.M3, 255, 255, 0)
    microbit.sleep(400)

    superbit.motor_control_dual(superbit.M1, superbit.M3, -255, -255, 0)
    microbit.sleep(400)

