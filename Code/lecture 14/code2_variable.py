x = 10
y = 20
def mean(a,b,c):
    global d, x
    x = 15
    d = (a+b+c)/3.0
    print x, y
    return d

average = mean(x,y,x+y)
print average

print d
print x, y
