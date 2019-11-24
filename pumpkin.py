# Шапка с подключаемыми модулями
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import math
import mcpi.vec3
import time
#Игра - поиск тыквы

# Описание функции для определения расстояния
# между двумя точками
def Distance(pos1, pos2):
    dx = pos2.x - pos1.x
    dy = pos2.y - pos1.y
    dz = pos2.z - pos1.z
    return math.sqrt(dx*dx + dy*dy + dz*dz)

#Сгенерировать тыкву в случайно точке
#на расстоянии 64 метров от Игрока

pumpkinId = 86
posPlayer = mc.player.getTilePos()
distance = 64
x = posPlayer.x + random.randint(-distance,distance)
y = posPlayer.y
z = posPlayer.z + random.randint(-distance,distance)
mc.setBlock(x,y,z,pumpkinId)
posPumpkin = mcpi.vec3.Vec3(x,y,z)

#Периодически сообщать Игроку стал он ближе
# к тыкве или нет
radius = Distance(posPlayer, posPumpkin)
while True:
    posPlayer = mc.player.getTilePos()
    newRadius = Distance(posPlayer, posPumpkin)
    if (newRadius < radius):
        mc.postToChat("Hot")
    else:
        mc.postToChat("Cold")
    radius = newRadius
    time.sleep(2)



    

















