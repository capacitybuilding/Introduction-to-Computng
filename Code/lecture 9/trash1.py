from cs1robots import *
import time
load_world("worlds/trash1.wld")
hubo=Robot()
hubo.set_pause(0.05)
time.sleep(0.05)
hubo.set_trace("red")
while hubo.front_is_clear():
    hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()
for i in range(2):
        hubo.turn_left()

while hubo.front_is_clear():
    hubo.move()
for i in range(3):
        hubo.turn_left()
hubo.move()
while hubo.carries_beepers():
    hubo.drop_beeper()
for i in range(2):
        hubo.turn_left()
hubo.move()
hubo.turn_left()
