from cs1graphics import *
stadium = Canvas(1200, 800)
stadium.setTitle('ASTU Stadium')
stadium.setBackgroundColor((69,139,0))

meda = Layer()
field = Rectangle(800, 400, Point(600, 400))
field.setBorderColor('white')
field.setFillColor((102,205,0))
field.setBorderWidth(3)
meda.add(field)

half_way_line = Path(Point(600, 200), Point(600,600))
half_way_line.setBorderColor('white')
half_way_line.setBorderWidth(3)
meda.add(half_way_line)

center_circle = Circle(70, Point(600, 400))
center_circle.setBorderColor('white')
center_circle.setBorderWidth(3)
meda.add(center_circle)

center_spot = Circle(3, Point(600, 400))
center_spot.setBorderColor('white')
center_spot.setBorderWidth(3)
center_spot.setFillColor('white')
meda.add(center_spot)

penality_area_left = Layer()
penality_area = Path(Point(200, 300),Point(300, 300),Point(300, 500),Point(200, 500))
penality_area.setBorderColor('white')
penality_area.setBorderWidth(3)
penality_area_left.add(penality_area)

goal_keeper_area = Path(Point(200, 350),Point(250, 350),Point(250, 450),Point(200, 450))
goal_keeper_area.setBorderColor('white')
goal_keeper_area.setBorderWidth(3)
penality_area_left.add(goal_keeper_area)

penality_spot = Circle(3, Point(275, 400))
penality_spot.setBorderColor('white')
penality_spot.setBorderWidth(3)
penality_spot.setFillColor('white')
penality_area_left.add(penality_spot)

penality_arc = Spline(Point(300, 360), Point(350, 400), Point(300, 440))
penality_arc.setBorderColor('white')
penality_arc.setBorderWidth(3)
penality_area_left.add(penality_arc)

meda.add(penality_area_left)

text = Text('ASTU STADIUM', 30, Point(600, 150))
text.setFontColor('white')
meda.add(text)

run_track = Layer()
track = Ellipse(1200, 700, Point(600, 400))
track.setBorderColor('red')
track.setBorderWidth(50)
run_track.add(track)

track1 = Ellipse(1200, 700, Point(600, 400))
track1.setBorderColor('white')
track1.setBorderWidth(3)
run_track.add(track1)


track2 = Ellipse(1180, 680, Point(600, 400))
track2.setBorderColor('white')
track2.setBorderWidth(3)
run_track.add(track2)

track3 = Ellipse(1220, 720, Point(600, 400))
track3.setBorderColor('white')
track3.setBorderWidth(3)
run_track.add(track3)

track4 = Ellipse(1160, 660, Point(600, 400))
track4.setBorderColor('white')
track4.setBorderWidth(3)
run_track.add(track4)

track5 = Ellipse(1240, 740, Point(600, 400))
track5.setBorderColor('white')
track5.setBorderWidth(3)
run_track.add(track5)

stadium.add(run_track)
stadium.add(meda)

 
