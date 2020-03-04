import mcpi.minecraft as minecraft
import mcpi.block as block
from minecraftshape import MinecraftMath3DShape
import time
 

 
# 连接到游戏
 
mc = minecraft.Minecraft.create()

mathshape = MinecraftMath3DShape(mc)


#半径
LENGTH=50

 
Middle = mc.player.getTilePos()

#mathshape.drawCurve1(Middle.x, Middle.y, Middle.z,LENGTH, 100,block.DIAMOND_BLOCK.id)
#mathshape.drawCurve1(Middle.x, Middle.y, Middle.z,LENGTH, 100,block.AIR.id)

#mathshape.drawCurve2(Middle.x, Middle.y+20, Middle.z,LENGTH, 100,block.DIAMOND_BLOCK.id)
#mathshape.drawCurve2(Middle.x, Middle.y+20, Middle.z,LENGTH, 100,block.AIR.id)

#mathshape.drawCurve3(Middle.x, Middle.y+20, Middle.z,LENGTH, 100,block.DIAMOND_BLOCK.id)
#mathshape.drawCurve3(Middle.x, Middle.y+20, Middle.z,LENGTH, 100,block.AIR.id)

mathshape.drawCurve4(Middle.x, Middle.y+50, Middle.z,LENGTH, 100,block.DIAMOND_BLOCK.id)
#mathshape.drawCurve4(Middle.x, Middle.y+50, Middle.z,LENGTH, 100,block.AIR.id)

#if buried,just shuttle
#mc.player.setTilePos(Middle.x+100,Middle.y+20,Middle.z+100)
