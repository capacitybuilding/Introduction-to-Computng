from cs1robots import *
load_world('worlds/sort1.wld')
hubo = Robot()
hubo.set_pause(0.2)
hubo.turn_left()
hubo.pick_beeper()
for i in range(6):
    hubo.move()
    hubo.pick_beeper()

for i in range(3):
    hubo.turn_left()
hubo.move()
for i in range(3):
    hubo.turn_left()
hubo.move()

for i in range(5):
    hubo.move()
    hubo.pick_beeper()


for i in range(3):
    hubo.turn_left()
hubo.move()

for i in range(2):
    hubo.turn_left()
