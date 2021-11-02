from cs1graphics import *
anis = Canvas()
anis.setWidth(600)
anis.setBackgroundColor((100, 200, 50))
anis.setHeight(400)
anis.setTitle('astu')

a = Point(100,100)
b = Point(200,200)
c = Point(300,200)
d = Point(300, 150)
p = Path(a,b,c)
p.addPoint(d)
# p.deletePoint(2)
# p.clearPoints()
p.setPoint(Point(300,300), 0)
# p.finalize()
# p.deletePoint()
anis.add(p)

t = Text('hello world', 30, Point(100,100))
t.setMessage('ASTU')
t.setFontSize(10)
t.setFontColor('red')
t.scale(3)
print t.getDimensions()
anis.add(t)







