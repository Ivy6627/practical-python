# bounce.py
#
# Exercise 1.5
height = 100
for i in range(1, 11):
    bounce_height = height*0.6
    height = bounce_height
    print(i, round(bounce_height, 4))
