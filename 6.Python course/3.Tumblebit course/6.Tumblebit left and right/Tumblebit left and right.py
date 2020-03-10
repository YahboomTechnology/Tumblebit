from microbit import *
import microbit
import superbit

display.show(Image.HAPPY)

while True:
    superbit.motor_control_dual(superbit.M1, superbit.M3, 0, 100, 0)
    microbit.sleep(500)

    superbit.motor_control_dual(superbit.M1, superbit.M3, 0, 0, 0)
    microbit.sleep(1000)

    superbit.motor_control_dual(superbit.M1, superbit.M3, 100, 0, 0)
    microbit.sleep(500)

    superbit.motor_control_dual(superbit.M1, superbit.M3, 0, 0, 0)
    microbit.sleep(1000)
