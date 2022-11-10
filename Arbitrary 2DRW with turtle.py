import turtle
t=turtle.Turtle()
from turtle import *

from random import randrange

for i in range(1000):
	angle=randrange(360)
	rt(angle)
	fd(20)