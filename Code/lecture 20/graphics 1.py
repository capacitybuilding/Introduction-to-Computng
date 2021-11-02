from cs1graphics import *
anis = Canvas()
anis.setWidth(600)
anis.setBackgroundColor((100, 200, 50))
anis.setHeight(400)
anis.setTitle('astu')
c = Circle(100, Point(200,200))
c.setRadius(50)

anis.add(c)

e = Ellipse(w = 100, h=60, centerPt=Point(50,50))
e.setWidth(50)
e.setHeight(100)
anis.add(e)

r = Rectangle(200, 100, Point(250,250))
r.setHeight(50)
r.setWidth(300)
anis.add(r)

s = Square(size=200, centerPt=Point(200,200))
s.setSize(50)
anis.add(s)






