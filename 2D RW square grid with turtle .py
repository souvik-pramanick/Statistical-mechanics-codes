import turtle
t=turtle.Turtle()
from turtle import *

import random
dot(5)   #starting point dot of size 5

for i in range(5000):
	n=random.randint(1,4)
	if n==1:
		fd(5)
	if n==2:
		bk(5)
	if n==1:
		rt(90)
		fd(5)
	if n==2:
		lt(90)
		fd(5)
		
dot(5) #last point



