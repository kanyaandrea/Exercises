import datetime
import random
l = []
l.append(random.randint(-30,50))
l.append(random.randint(-30,50))
l.append(random.randint(-30,50))
l.append(random.randint(-30,50))
l.append(random.randint(-30,50))
l.append(random.randint(-30,50))
l.append(random.randint(-30,50))
l.append(random.randint(-30,50))
x = 0
while x < 8:
    f = (l[x] * 1.8) + 32
    print("celsius: " + str(l[x]) + " fahrenheit: " + str(f))
    x = x + 1
l.append(random.randint(-30,50))
l.append(random.randint(-30,50))
l.append(random.randint(-30,50))
l.append(random.randint(-30,50))
l.append(random.randint(-30,50))
while x < 13:
    f = (l[x] * 1.8) + 32
    print("celsius: " + str(l[x]) + " fahrenheit: " + str(f))
    x = x + 1
