from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
p=mc.player.getPos()
x=p.x
y=p.y
z=p.z + 5
startZ = z

for j in range(10):
    for i in range(10):
        #куб
        mc.setBlocks(x,  y,  z,  x+10,y+10,z+10,5)
        #пустота в кубе
        mc.setBlocks(x+1,y+1,z+1,x+9, y+9, z+9, 0)
        #крыша
        mc.setBlocks(x,  y+10,z, x+10,y+10,z+10,20)
        #пол
        mc.setBlocks(x,  y,   z, x+10,y,   z+10,20)
        #телепорт в центр комнаты
        #DOOR
        mc.setBlock(x+5,y,z,5)
        mc.setBlock(x+5,y+1,z,64)
        mc.setBlock(x+5,y+2,z,64)
        z += 20
        time.sleep(0)
    x += 20
    z = startZ