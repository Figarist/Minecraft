import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

pos= mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

time.sleep(10)

pos= mc.player.getTilePos()
x1 = pos.x
y1 = pos.y
z1 = pos.z

mc.postToChat("Player has moved x = " + str(x1-x)+", y = "
              + str(y1-y) + ", z = "+ str(z1-z))