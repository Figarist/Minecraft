import mcpi.minecraft as minecraft
from random import *
mc = minecraft.Minecraft.create()

pos= mc.player.getPos()

pos.x+=1
for i in range(30):
    mc.setBlock(pos.x,pos.y+i,pos.z,randint(0,100),0)



