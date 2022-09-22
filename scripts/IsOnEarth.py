from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
for i in range(100):
    time.sleep(1)
    pos = mc.player.getTilePos() # позиция игрока
    x = pos.x
    y = pos.y
    z = pos.z
    highestBlockY = mc.getHeight(x, z) # самый высокий блок
    mc.postToChat("player y = "+str(y))
    mc.postToChat("block lower y = "+str(highestBlockY))
    if y-1>highestBlockY:
        mc.postToChat("player in air")
    else:
        mc.postToChat("player on block")
