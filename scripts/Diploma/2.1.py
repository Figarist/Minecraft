import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()


while True:
    pos= mc.player.getTilePos()
    block = mc.getBlock(pos.x,pos.y-1,pos.z)
    print(block)
    if block==9:
        mc.setBlock(pos,1)
        mc.player.setPos(pos.x,pos.y+5,pos.z)
        