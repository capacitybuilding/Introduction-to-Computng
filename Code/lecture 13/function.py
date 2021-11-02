from cs1robots import *
create_world()
h = Robot()
h.set_pause(0.5)
def right():
    for i in range(3):
        h.turn_left()
def go():
    for i in range(9):
        h.move()

h.turn_left()
go()
right()
go()
right()
go()
right()
go()
