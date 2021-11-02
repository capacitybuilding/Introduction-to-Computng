from cs1robots import *
import time
load_world("worlds/hurdles1.wld")
hubo=Robot()
hubo.set_pause(0.05)
time.sleep(0.5)
hubo.set_trace("green")
while not hubo.on_beeper():
    if hubo.right_is_clear():
        for i in range(3):
            hubo.turn_left()
        hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
hubo.pick_beeper()

