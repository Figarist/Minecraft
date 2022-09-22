import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

pos= mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlock(x+1,y,z,5,0)
mc.setBlock(x-1,y,z,5,0)
mc.setBlock(x,y,z-1,5,0)
mc.setBlock(x,y,z+1,5,0)
mc.setBlock(x+1,y,z+1,5,0)
mc.setBlock(x+1,y,z-1,5,0)
mc.setBlock(x-1,y,z+1,5,0)
mc.setBlock(x-1,y,z-1,5,0)