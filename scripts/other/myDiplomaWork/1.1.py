import mcpi.minecraft as minecraft 
mc = minecraft.Minecraft.create()

x = int(input("Введіть значення X = "))

y = int(input("Введіть значення Y = "))
while y<0:
    print("Невірне значення Y")
    y = int(input("Введіть значення Y = "))
    
z = int(input("Введіть значення Z = "))

mc.player.setPos(x,y,z)
mc.postToChat("Teleported to "+str(x)+" "+str(y)+" "+str(z))
print("Гравця телепортовано на координати ",x,y,z)
