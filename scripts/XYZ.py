from mcpi.minecraft import Minecraft

mc = Minecraft.create()
if input("enter center") == "center":
    mc.player.setPos(0, 100, 0)
    for i in range(500):
        '''X'''
        mc.setBlock(0 + i, 100, 0, 10)
        '''Y'''
        mc.setBlock(0, 100 + i, 0, 10)
        '''Z'''
        mc.setBlock(0, 100, 0 + i, 10)

        '''XY'''
        mc.setBlock(0 + i, 100 + i, 0, 8)
        '''YZ'''
        mc.setBlock(0, 100 + i, 0 + i, 8)
        '''XYZ'''
        mc.setBlock(0 + i, 100 + i, 0 + i, 8)
else:
    x, y, z = mc.player.getPos()
    for i in range(500):
        '''X'''
        mc.setBlock(x + i, y, z, 10)
        '''Y'''
        mc.setBlock(x, y + i, z, 10)
        '''Z'''
        mc.setBlock(z, y, x + i, 10)

        '''XY'''
        mc.setBlock(x + i, y + i, z, 8)
        '''YZ'''
        mc.setBlock(x, y + i, z + i, 8)
        '''XYZ'''
        mc.setBlock(x + i, y + i, z + i, 8)
