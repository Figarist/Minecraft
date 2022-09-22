from mcpi.minecraft import Minecraft
from mcpi import block
from minecraftstuff import MinecraftTurtle

mc = Minecraft.create()
pos = mc.player.getPos()

# create minecraft turtle
steve = MinecraftTurtle(mc, pos)
steve.speed(0)
# draw a pentagon
for i in range(255):
    steve.forward(1)
    steve.up(90)
    steve.forward(1)
    steve.down(90)
