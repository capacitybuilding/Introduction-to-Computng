for i in range(7):
    if i == 5:
        break
    print i


for i in range(8):
    if i%2 == 0:
        continue
    print i


for i in range(10):
    if i*i > 50:
        break
    elif i%3 == 0:
        continue
    else:
        print i*i
