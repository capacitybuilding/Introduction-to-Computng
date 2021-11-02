from cs1graphics import *
anis = Canvas(1000, 500, (100, 200, 50))

car = Layer()


c = Circle(50, Point(300,300))
car.add(c)

c.setFillColor('red')
c.setDepth(45)

r = Rectangle(200, 100, Point(300,300))
car.add(r)
r.setFillColor('white')
r.setDepth(46)
r.setBorderColor((255,255,255))
r.setBorderWidth(3)

r.rotate(-30)

p = Path(Point(100,100), Point(100, 200), Point(200,200))
anis.add(p)
p.rotate(30)
p.scale(0.5)

r2 = r.clone()
anis.add(r2)
r2.moveTo(100,100)

anis.add(car)
car.move(100,-100)



