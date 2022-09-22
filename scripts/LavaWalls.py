from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
x, y, z = mc.player.getPos()
y += 100
for i in range(100):
    time.sleep(0.1)
    '''стена первая Х'''
    mc.setBlock(x + i, y, z, 10)
    '''стена первая Z'''
    mc.setBlock(x, y, z + i, 10)
    '''стена вторая Х'''
    mc.setBlock(x + i, y, z, 10)
    '''стена вторая Z'''
    mc.setBlock(x, y, z + i, 10)
