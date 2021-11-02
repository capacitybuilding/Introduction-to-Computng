from cs1robots import *
import time
create_world()
anis = Robot()

time.sleep(2)
anis.set_pause(1)
anis.set_trace('red')

anis.move()
anis.move()
