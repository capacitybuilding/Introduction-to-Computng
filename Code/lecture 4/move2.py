from cs1robots import *
import time
create_world()
anis = Robot()

time.sleep(.5)
anis.set_pause(.1)
anis.set_trace('red')

for i in range(9):
    anis.move()
anis.turn_left()
for i in range(9):
    anis.move()
