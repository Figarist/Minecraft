import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

pos= mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.postToChat(x)
mc.postToChat(y)
mc.postToChat(z)