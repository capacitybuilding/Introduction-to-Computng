from cs1robots import *
create_world()
rim = Robot()
rim.set_pause(0.5)
while rim.front_is_clear():
    rim.move()
