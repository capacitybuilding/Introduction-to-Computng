from cs1robots import *
import time
load_world("worlds/rain1.wld")
hubo=Robot(beepers=6 , avenue=3 , street=6 , orientation="S")
hubo.set_trace("red")
hubo.set_pause(0.02)
time.sleep(1)
hubo.drop_beeper()
hubo.move()
while not hubo.on_beeper():
    if hubo.right_is_clear():
        hubo.drop_beeper()
        hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
        
