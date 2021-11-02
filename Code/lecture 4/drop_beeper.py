from cs1robots import *
import time
create_world()
anis = Robot(beepers = 1)

time.sleep(.5)
anis.set_pause(.1)
anis.set_trace('red')

for i in range(9):
    anis.move()
anis.drop_beeper()
anis.turn_left()
anis.turn_left()
for i in range(9):
    anis.move()
