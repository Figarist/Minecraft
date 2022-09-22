import mcpi.minecraft as minecraftmc = minecraft.Minecraft.create()

pos= mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z


ID = int(input())
mc.setBlock(x+1,y,z,20,0)
    


