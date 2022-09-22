from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()


def railLong(n):
    id_block = 20
    id_road = 173
    id_rail = 27
    id_red = 75
    id_air = 0
    id_lamp = 89
    p = mc.player.getPos()
    for i in range(n):
        # centr
        mc.setBlock(p.x, p.y, p.z + i, id_road)  # дорога под колией
        mc.setBlock(p.x, p.y + 1, p.z + i, id_rail)  # колия
        mc.setBlock(p.x, p.y + 2, p.z + i, id_air)  # воздух
        mc.setBlock(p.x, p.y + 3, p.z + i, id_air)  # воздух
        mc.setBlock(p.x, p.y + 4, p.z + i, id_air)  # воздух
        mc.setBlock(p.x, p.y + 5, p.z + i, id_air)  # воздух
        mc.setBlock(p.x, p.y + 6, p.z + i, id_block)  # верхний люк
        # стена 1
        mc.setBlock(p.x - 1, p.y, p.z + i, id_lamp)  # фонарь
        mc.setBlock(p.x - 1, p.y + 1, p.z + i, id_block)  # стена из стекла
        mc.setBlock(p.x - 1, p.y + 2, p.z + i, id_block)  #
        mc.setBlock(p.x - 1, p.y + 3, p.z + i, id_block)  #
        mc.setBlock(p.x - 1, p.y + 4, p.z + i, id_block)  #
        mc.setBlock(p.x - 1, p.y + 5, p.z + i, id_block)  #
        # стена 2
        mc.setBlock(p.x + 1, p.y, p.z + i, id_lamp)  # фонарь
        mc.setBlock(p.x + 1, p.y + 1, p.z + i, id_block)  # стена из стекла
        mc.setBlock(p.x + 1, p.y + 2, p.z + i, id_block)  #
        mc.setBlock(p.x + 1, p.y + 3, p.z + i, id_block)  #
        mc.setBlock(p.x + 1, p.y + 4, p.z + i, id_block)  #
        mc.setBlock(p.x + 1, p.y + 5, p.z + i, id_block)  #
        if i % 8 == 0:  # здесь мы проверяем на каком сейчас мы блоке
            # если число делится на 8, то мы
            # ставим блок факела,под факелом другой блок( не фонарь)
            # на фонаре факел на ставится
            # и сбоку от факела ставим стекло, чтобы шахта работала под водой
            # была полностью герметичной
            mc.setBlock(p.x - 1, p.y, p.z + i, id_road)  # меняем блок фонаря на другой блок,чтобі стоял
            mc.setBlock(p.x - 2, p.y + 1, p.z + i, id_block)  # ставим блок стекла правее факела, для герметичности
            mc.setBlock(p.x - 1, p.y + 1, p.z + i, id_red)  # ставим наконец факел


railLong(2000)  # запускаем нашу функцию с нашим аргументов(длина дороги)
