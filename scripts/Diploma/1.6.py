import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

pos= mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z


a = input()
if a=='x':
    mc.player.setPos(x+int(input()),y,z)
elif a=='y':
    mc.player.setPos(x,y+int(input()),z)
else:
    mc.player.setPos(x,y,z+int(input()))
    

