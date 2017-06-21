import random
import math
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]#list of number from 10 to 100 by 10
t = 0#t is zero now
if a[0] % 20:
    t += a[0]
    print(t)
if a[1] % 20:
    t += a[1]
    print(t)
if a[2] % 20:
    t += a[2]
    print(t)
if a[3] % 20:
    t += a[3]
    print(t)
if a[4] % 20:
    t += a[4]
if a[5] % 20:
    t += a[5]
if a[6] % 20:
    t += a[6]
if a[7] % 20:
    t += a[7]
if a[8] % 20:
    t += a[8]
if a[9] % 20:
    t += a[9]
print("Summation of number divisible by 20 is: " + str(t))
