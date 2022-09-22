import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

pos= mc.player.getPos()
x = pos.x + 5
y = pos.y
z = pos.z

size,ID = map(int,input().split())

mc.setBlocks(x,y,z,x+size,y+size,z+size,ID,0)


