import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

pos= mc.player.getPos()

for i in range(10):
    mc.setBlock(pos.x,pos.y+i,pos.z,1,0)


