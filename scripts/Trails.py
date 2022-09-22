from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
c=0
for i in range(100):
    time.sleep(0.1)
    p = mc.player.getPos()
    if c ==0:
        mc.setBlock(p.x,p.y,p.z,10)
        c=1
    elif c ==1:
        mc.setBlock(p.x,p.y,p.z,10)
        c=0
