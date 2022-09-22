import mcpi.minecraft as minecraft
from random import *
from time import *
mc = minecraft.Minecraft.create()

x = randint(-100000,100000)
y = randint(70,200)
z = randint(-100000,100000)
mc.player.setPos(x,y,z)
sleep(10)
x = randint(-100000,100000)
y = randint(70,200)
z = randint(-100000,100000)
mc.player.setPos(x,y,z)
sleep(10)
x = randint(-100000,100000)
y = randint(70,200)
z = randint(-100000,100000)
mc.player.setPos(x,y,z)
sleep(10)