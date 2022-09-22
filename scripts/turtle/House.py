from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftTurtle
from minecraftstuff import MinecraftDrawing

mc = Minecraft.create()
pos = mc.player.getTilePos()
x=round(pos.x)
y=round(pos.y)
z=round(pos.z)
t= MinecraftTurtle(mc, pos)
d = MinecraftDrawing(mc)
a=10
t.speed(0)
t.forward(a)
t.left(90)
t.forward(a)
t.left(90)
t.forward(a)
t.left(90)
t.forward(a)
t.setposition(x,y,z)
d.drawLine(x,      y-1,      z,x+a//2, y-1, z+a//2, 110,0)
d.drawLine(x+a//2, y-1, z+a//2,   x+a, y-1,      z, 110,0)
t.setposition(x+5,y,z-10)
t.forward(5)