import random
import math

a = []
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
c= 0
for i in range(0, 10):#this is the loop!
    if a[i] % 7 == 0:
        c += 1
    elif a[i] % 5 == 0:
        c += 1
    elif a[i] % 3 == 0:
        c += 1
    if a[i] % 7 == 0:
        print(str(a[i]) + " is divisible by 7 or 5 or 3!")
    elif a[i] % 5 == 0:
        print(str(a[i]) + " is divisible by 7 or 5 or 3!")
    elif a[i] % 3 == 0:
        print(str(a[i]) + " is divisible by 7 or 5 or 3!")
print("We found " + str(c) + " numbers divisible by 7 or 5 or 3!")
